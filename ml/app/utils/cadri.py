import os
import cv2
import uuid
from moviepy.editor import VideoFileClip, CompositeVideoClip


def detect_faces_and_crop(video_path, output_video_path, soap=False):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Шаг 1: Проверка количества кадров
    cap = cv2.VideoCapture(video_path)
    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    print(f'Checking Video: {video_path} | Frames: {frames} | FPS: {fps}')

    # Шаг 2: Если количество кадров равно нулю, создаем временное видео
    if frames == 0:
        print(f'No frames data in video {video_path}, trying to convert this video..')

        # Создаем временное видео
        temp_video_path = f"app/temp/fixVideo_{uuid.uuid4()}.avi"
        writer = cv2.VideoWriter(
            temp_video_path,
            cv2.VideoWriter_fourcc(*'DIVX'),
            fps,
            (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        )

        while True:
            ret, frame = cap.read()
            if ret:
                writer.write(frame)
            else:
                break

        cap.release()
        writer.release()
        print("Stopping video writer")

        # Обновляем путь к видео для дальнейшей обработки
        video_path = temp_video_path
        cap = cv2.VideoCapture(video_path)
        frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        print(f'Converted video has {frames} frames.')

    # Получаем параметры видео
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    new_width = frame_height * 9 // 16
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fragment_uuid = str(uuid.uuid4())
    output_video = r"app/temp/" + fragment_uuid + r".mp4"
    out = cv2.VideoWriter(output_video, fourcc, fps, (new_width, frame_height))

    last_face_coordinates = None
    frames_without_face = 0
    max_frames_without_face = 200
    last_len = -1

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        if len(faces) == 1 and last_len != len(faces):
            (x, y, w, h) = faces[0]
            last_face_coordinates = (x, y, w, h)
            frames_without_face = 0
            last_len = len(faces)
        elif last_face_coordinates:
            if last_len != len(faces):
                frames_without_face += 1

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

    # Обработка аудио и видео
    video_clip = VideoFileClip(output_video)
    original_video = VideoFileClip(video_path)
    final_video = video_clip.set_audio(original_video.audio)

    if soap:
        overlay_clip = VideoFileClip("/temp/soap.mp4").without_audio()
        overlay_clip_resized = overlay_clip.resize(0.5)
        overlay_clip_resized = overlay_clip_resized.set_duration(final_video.duration)
        overlay_position = (0, 800)
        final_clip = CompositeVideoClip([final_video, overlay_clip_resized.set_position(overlay_position)])
        final_clip.write_videofile(output_video_path, codec="libx264")
    else:
        final_video.write_videofile(output_video_path, codec="libx264")
    # Удаляем временное видео, если оно было создано
    if frames == 0:
        os.remove(temp_video_path)


#print(detect_faces_and_crop("finder_viral_moments/reels_1_s31.mp4","output.mp4"))