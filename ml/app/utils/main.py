
import app.utils.finder_viral_moments.finderviral as fv
import app.utils.cadri as cadr
import app.utils.subscription as subscription
from app.core.config import settings
import uuid
import os
import cv2
from moviepy.editor import VideoFileClip,CompositeVideoClip
import uuid

folder="app/temp"



def detect_faces_and_crop(video_path, output_video_path,soap=False):

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


    cap = cv2.VideoCapture(video_path)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    new_width = frame_height * 9 // 16

    fourcc = cv2.VideoWriter_fourcc(*'H264')
    fragment_uuid = str(uuid.uuid4())
    output_video = r"app/temp/"+fragment_uuid+r".mp4"
    #output_video = fragment_uuid + r".mp4"
    out = cv2.VideoWriter(output_video, fourcc, fps, (new_width, frame_height))

    if os.path.exists(output_video):
        print(f"Видео успешно сохранено: {output_video}")
    else:
        print(f"Ошибка: файл {output_video} не был создан.")
    last_face_coordinates = None
    frames_without_face = 0
    max_frames_without_face = 200
    last_len = -1
    n=False
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)


        if len(faces) == 1 and last_len!=len(faces):
            (x, y, w, h) = faces[0]
            last_face_coordinates = (x, y, w, h)
            frames_without_face = 0
            last_len=len(faces)

        elif last_face_coordinates:
            if last_len!=len(faces):

                frames_without_face += 1
                #print(f"+{1}={frames_without_face} was{last_len,len(faces)}")

        if frames_without_face > max_frames_without_face:
            last_face_coordinates = None


        if last_face_coordinates:
            (x, y, w, h) = last_face_coordinates
            center_x = x + w // 2

            left_x = max(0, center_x - new_width // 2)
            right_x = min(frame_width, center_x + new_width // 2)


            cropped_frame = frame[:, left_x:right_x]
            resized_frame = cv2.resize(cropped_frame, (new_width, frame_height))

        else:
            left_x = (frame_width - new_width) // 2
            cropped_frame = frame[:, left_x:left_x + new_width]
            resized_frame = cv2.resize(cropped_frame, (new_width, frame_height))


        out.write(resized_frame)

    cap.release()
    out.release()

    video_clip = VideoFileClip(output_video)
    original_video = VideoFileClip(video_path)
    final_video = video_clip.set_audio(original_video.audio)


    ###
    if soap:
        overlay_clip = VideoFileClip("/temp/soap.mp4").without_audio()
        overlay_clip_resized = overlay_clip.resize(0.5)
        overlay_clip_resized = overlay_clip_resized.set_duration(final_video.duration)
        overlay_position = (0, 800)
        final_clip = CompositeVideoClip([final_video, overlay_clip_resized.set_position(overlay_position)])


        final_clip.write_videofile(output_video_path, codec="libx264")
    else:
        final_video.write_videofile(output_video_path, codec="libx264")


def make_video(id,input_video,title,soap):
    directories_to_check = [
        f"{folder}/edited/{id}",
        f"{folder}/thumbnails"
    ]

    # Проверка наличия директорий и их создание, если не существуют
    for directory in directories_to_check:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Создана директория: {directory}")
        else:
            print(f"Директория уже существует: {directory}")

    cadr_name = f"{folder}/edited/{id}/cadr.mp4"
    res_name = f"{folder}/edited/{id}/edited.mp4"
    res_thumbnail_name = f"{folder}/thumbnails/{id}.png"
    if soap=="0":
        a=False
    else:
        a=True
    cadr.detect_faces_and_crop(input_video,cadr_name,a)
    #cadr_name=input_video
    print(cadr_name)
    #[video_duration_str, wordlevel_info, subtitles_text]

    data = subscription.process_video_with_subtitles(cadr_name, title,res_thumbnail_name,output_filename=res_name)
    return {
        "resname": res_name,
        "duration": data[0],
        "thumbnail": res_thumbnail_name,
        "transcriptionRaw": data[2],
        "transcriptionTimecodes": data[1]
    }




def change_video(id,transcriptionTimecodes,title):

    cadr_name = f"{folder}/edited/{id}/cadr.mp4"
    res_name = f"{folder}/edited/{id}/edited.mp4"
    res_thumbnail_name = f"{folder}/edited/{id}/preview.png"

    #[video_duration_str, wordlevel_info, subtitles_text]
    data=subscription.process_video_with_subtitles(cadr_name,title,res_thumbnail_name,output_filename=res_name, new_subscription=transcriptionTimecodes)
    return {
        "resname":res_name,
        "duration":data[0],
        "thumbnail":res_thumbnail_name,
        "transcriptionRaw":data[2],
        "transcriptionTimecodes":data[1]
            }


def generate_metrics_description(metric_scores):
    description_parts = []

    for score_pair in metric_scores:  # Перебираем список
        metric, score = score_pair  # Получаем вопрос и оценку
        # Используем условие для определения метрики
        if "emotional response" in metric:
            description_parts.append(f"Эмоциональная реакция: {score}/10")
        elif "ease of understanding" in metric:
            description_parts.append(f"Легкость восприятия: {score}/10")
        elif "uniqueness of the content" in metric:
            description_parts.append(f"Уникальность контента: {score}/10")
        elif "interaction of the text with the reader" in metric:
            description_parts.append(f"Взаимодействие с читателем: {score}/10")
        elif "clarity of the message" in metric:
            description_parts.append(f"Ясность сообщения: {score}/10")
        elif "connection with popular culture" in metric:
            description_parts.append(f"Связь с популярной культурой: {score}/10")
        elif "potential for discussion" in metric:
            description_parts.append(f"Потенциал для обсуждения: {score}/10")
        elif "character of the narration" in metric:
            description_parts.append(f"Характер повествования: {score}/10")

    return "\n".join(description_parts)
def find_moments(id,input_video,soap):
    base_dir = f"{folder}/{id}/"

    dir_viral_moments=f"{base_dir}viral_after_find/"
    os.makedirs(dir_viral_moments, exist_ok=True)
    print("start viral moments ===================")
    data=fv.process_video(input_video,base_dir)
    print("viral moments ready==========================")
    files_and_folders = os.listdir(dir_viral_moments)
    mp4_files = [f for f in files_and_folders if f.endswith('.mp4') and os.path.isfile(os.path.join(dir_viral_moments, f))]
    print(mp4_files)
    data_res=[]
    metrics_data=[]
    metric_sums = {
        "emotional_response": 0,
        "ease_of_understanding": 0,
        "uniqueness_of_content": 0,
        "interaction_with_reader": 0,
        "clarity_of_message": 0,
        "connection_with_popular_culture": 0,
        "potential_for_discussion": 0,
        "narration_character": 0
    }
    for idx, moment in enumerate(mp4_files):
        print(idx,moment)
        fragment_uuid = str(uuid.uuid4())
        link=f"{dir_viral_moments}{moment}"
        data_video=make_video(fragment_uuid, link,data[idx]["chunk_title"],soap)
        description_metr=generate_metrics_description(data[idx]["metric_score"])
        metric_score = data[idx]["metric_score"]
        metrics_data.append(metric_score)


        for key in metric_sums.keys():
            if key in metric_score:
                metric_sums[key] += metric_score[key]
        res={
                    "uuid": fragment_uuid,
                    "fragmentTitle": data[idx]["chunk_title"],

                    "videoLink": f"{settings.SERVER_LINK}video/{data_video['resname']}",
                    "thumbnail": f"{settings.SERVER_LINK}video/{data_video['thumbnail']}",
                    "duration": data_video['duration'],
                    "viralScore": data[idx]["total_score"],
                    "viralDescription": description_metr,
                    "tags": [
                        "тег1",
                        "тег2",
                        "тег3"
                    ],
                    "transcriptionRaw": data_video["transcriptionRaw"],
                    "transcriptionTimecodes": data_video["transcriptionTimecodes"]
                }
        data_res.append(res)
    return [data_res,metric_sums]