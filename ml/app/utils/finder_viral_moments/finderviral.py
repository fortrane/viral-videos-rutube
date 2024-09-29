from app.utils.finder_viral_moments.transcribing_module.ts import audio_to_text, find_time_range
from app.utils.finder_viral_moments.title_and_metrics.viral_metric import evaluate_text
from app.utils.finder_viral_moments.title_and_metrics.text_analyzer import generate_chunk_title
from moviepy.video.io.VideoFileClip import VideoFileClip
from app.utils.finder_viral_moments.title_and_metrics import tag_gen


def cut_video(input_file: str, output_file: str, start_time: str, end_time: str):
    def time_to_seconds(time_str):
        h, m, s = map(float, time_str.split(':'))
        return h * 3600 + m * 60 + s

    with VideoFileClip(input_file) as video:
        start_sec = time_to_seconds(start_time)
        end_sec = time_to_seconds(end_time)
        video_subclip = video.subclip(start_sec, end_sec)
        video_subclip.write_videofile(output_file, codec='libx264', audio_codec='aac')


def process_video(video,path, fillter_score=0, max_tokens=450):
    print("transcription start============")
    transcription = audio_to_text(video)
    print("transcription ready============")
    evaluted_text = evaluate_text(transcription['only_t'], max_tokens=max_tokens)

    processed_chunks = []

    for idx, item in enumerate(evaluted_text):
        total_score = sum(int(score[1]) for score in item['chunk_score'])

        if total_score > fillter_score:
            processed_chunk = {}

            chunk_title = generate_chunk_title(item['chunk'])
            print("chunk_title ready============")
            chunk_timestemps = find_time_range(timestamps=transcription['with_ts'], search_text=item['chunk'])
            print("chunk_timestemps ready============")
            tags = tag_gen.generate_tags(item['chunk'])
            print("tag_gen ready============")

            start_time, end_time = chunk_timestemps

            output_video_file = f"{path}/viral_after_find/reels_{idx + 1}_s{total_score}.mp4"
            cut_video(video, output_video_file, start_time, end_time)

            processed_chunk['chunk'] = item['chunk']
            processed_chunk['chunk_title'] = chunk_title
            processed_chunk['chunk_timestemps'] = chunk_timestemps
            processed_chunk['total_score'] = total_score
            processed_chunk['metric_score'] = item['chunk_score']
            processed_chunk['output_video_file'] = output_video_file
            processed_chunk['tags'] = tags

            processed_chunks.append(processed_chunk)


    print(processed_chunks)

    return processed_chunks



#input_video = "test/video.mp4"

#process_video('govno-video.mp4', path=r'C:\Users\Admin\PycharmProjects\pythonProject\viral_clips_hackton\app\utils\finder_viral_moments')
