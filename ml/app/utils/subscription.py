import os
import ffmpeg
import whisper
import json
import cv2
from datetime import timedelta
from moviepy.editor import TextClip, CompositeVideoClip, VideoFileClip,ImageClip
emoji_image_folder = "app/utils/emodj/"
emoji = {
    "u26A1.png": ["⚡️", "ты", "энергия", "молния", "разряд", "электричество", "вспышка", "заряд", "удар", "импульс", "интенсивность", "сила", "шок", "искры"],
    "u1F525.png": ["🔥", "огонь", "пламя", "жар", "тепло", "горение", "искра", "пожар", "воспламенение", "гореть", "интенсивность", "сжигать", "страсть"],
    "u1F4A7.png": ["💧", "вода", "капля", "влага", "жидкость", "дождь", "роса", "слеза", "влага", "увлажнение", "чистота", "свежесть", "океан"],
    "u1F31F.png": ["🌟", "звезда", "свет", "сияние", "блеск", "луч", "звёздность", "гламур", "искриться", "яркость", "орел", "популярность", "фантазия"],
    "u1F32A.png": ["🌪", "вихрь", "торнадо", "буря", "шторм", "смерч", "ветер", "катастрофа", "хаос", "порыв", "ветровой", "неистовство", "разрушение"],
    "u1F308.png": ["🌈", "радуга", "цвета", "яркий", "свет", "лучи", "спектр", "надежда", "гармония", "красота", "позитив", "разноцветие", "мечта"],
    "u2744.png": ["❄️", "снег", "снежинка", "холод", "мороз", "лед", "зима", "заморозки", "иней", "заснеженный", "снегопад", "ледяной", "морозный"],
    "u1F4A1.png": ["💡", "свет", "лампа", "идея", "озарение", "освещение", "яркость", "изобретение", "новаторство", "находка", "вдохновение", "включение", "мысль"],
    "u1F30A.png": ["🌊", "волна", "океан", "море", "прилив", "течение", "водопад", "водная гладь", "шторм", "поток", "глубина", "волнующий", "разлив"],
    "u1F30D.png": ["🌍", "земля", "планета", "глобус", "мир", "экология", "природа", "окружающий мир", "климат", "экосистема", "экология", "материк", "континент"],
    "u1F31E.png": ["🌞", "солнце", "лучи", "свет", "тепло", "солнечный", "яркий", "рассвет", "жар", "дневной свет", "светило", "солнечность", "лето"],
    "u1F343.png": ["🍃", "листья", "природа", "зелень", "растение", "ветерок", "дерево", "флора", "экологичность", "свежесть", "естественность", "ветер", "экосистема"],
    "u23F0.png": ["⏰", "время", "будильник", "часы", "таймер", "секунды", "минуты", "срок", "точность", "дедлайн", "ждать", "пунктуальность", "поспешить"],
    "u1F680.png": ["🚀", "ракета", "космос", "взлет", "скорость", "полёт", "космический корабль", "миссия", "орбита", "звёзды", "ускорение", "космодром", "технология"],
    "u1F3C6.png": ["🏆", "известных","победим", "трофей", "победа", "награда", "успех", "достижение", "чемпион", "кубок", "лидерство", "триумф", "герой", "признание", "соревнование"],
    "u1F3AF.png": ["🎯", "цель", "мишень", "фокус", "успех", "достижение", "меткость", "попадание", "намерение", "план", "прицел", "точность", "задача"],
    "u1F389.png": ["🎉", "праздник", "торжество", "радость", "вечеринка", "увеселение", "салют", "фейерверк", "отдых", "яркость", "забава", "торжество", "событие"],
    "u2764.png": ["❤️", "любовь", "сердце", "чувство", "привязанность", "симпатия", "романтика", "страсть", "влюблённость", "сердечность", "забота", "эмоции", "нежность"],
    "u1F60E.png": ["😎", "круто", "стиль", "уверенность", "харизма", "мода", "расслабленность", "крутой", "беззаботность", "прохлада", "смелость", "отдых", "шик"],
    "u1F916.png": ["🤖", "робот", "технология", "искусственный интеллект", "механика", "автомат", "инновации", "будущее", "машина", "автоматизация", "электронный", "программирование", "кибер"],
    "u1F6A8.png": ["🚨", "тревога", "сигнал", "авария", "опасность", "предупреждение", "полиция", "экстренно", "сирена", "красный свет", "внимание", "чрезвычайная ситуация", "экстренное"],
    "u1F4A3.png": ["💣", "бомба", "взрыв", "опасность", "катастрофа", "разрушение", "взрывоопасный", "детонация", "шок", "кризис", "смертельный", "катаклизм", "трагедия"],
    "u1F4C8.png": ["📈", "рост", "успех", "прогресс", "график", "увеличение", "экономика", "подъём", "развитие", "финансы", "тренд", "статистика", "достижение"],
    "u1F3B5.png": ["🎵", "музыка", "мелодия", "звук", "ритм", "песня", "нотка", "композиция", "звучание", "гармония", "музыкальный", "певец", "инструмент"],
    "u1F451.png": ["👑", "корона", "король", "власть", "лидерство", "авторитет", "величие", "монарх", "престиж", "статус", "трон", "господство", "слава"],
    "u1F9E0.png": ["🧠", "мозг", "ум", "интеллект", "мышление", "размышление", "гениальность", "логика", "анализ", "разум", "осознанность", "креативность", "решение"],
    "u1F3AC.png": ["🎬", "кино", "съёмка", "режиссура", "кадр", "фильм", "кинематограф", "видеоролик", "камера", "сцена", "монтаж", "кинопроизводство", "режиссёр"],
    "u1F47E.png": ["👾", "игра", "пришелец", "вирус", "видеоигры", "киберспорт", "монстр", "виртуальный", "гейминг", "враждебный", "цифровой", "геймер", "фантастика"],
    "u1F465.png": ["👥", "люди", "группа", "вместе", "друзья", "коллектив", "общество", "взаимодействие", "сотрудничество", "команда", "социальность"],
    "u1F464.png": ["👤", "человек", "персона", "индивидуальность", "личность", "одиночество", "одиночка", "профиль", "идентичность", "одиночество"],
    "u1F46A.png": ["👪", "семья", "родители", "дети", "связь", "близкие", "любовь", "поддержка", "единство", "дома", "общение"],
    "u1F914.png": ["🤔", "думаю", "задумчивость", "вопрос", "мысль", "сомнение", "размышление", "неуверенность", "загадка", "идеи", "рефлексия", "анализ"],
    "u1F929.png": ["🤩", "восхищение", "супер", "удивление", "восторг", "экстаз", "радость", "успех", "блеск", "популярность", "звёзды", "счастье"],
    "u1F631.png": ["😱", "страх", "ужас", "паника", "шок", "испуг", "крик", "волнение", "сюрприз", "пугающе", "напряжённость", "катастрофа"],
    "u1F440.png": ["👀", "глаза", "внимание", "наблюдение", "взор", "смотрю", "увидеть", "фокус", "взгляд",
                   "внимательность"],
    "u1F48E.png": ["💎", "бриллиант", "драгоценность", "сокровище", "ценность", "красота", "шик", "роскошь", "богатство",
                   "элегантность", "исключительность"],
    "u1F98B.png": ["🦋", "бабочка", "красота", "лёгкость", "природа", "преобразование", "изящество", "метаморфоза",
                   "цветение", "свобода"],
    "u1F340.png": ["🍀", "удача", "клевер", "счастье", "везение", "надежда", "благополучие", "возможности", "судьба",
                   "четырехлистник"],
    "u1F4A2.png": ["💢", "гнев", "ярость", "недовольство", "эмоции", "злость", "негодование", "агрессия", "буря",
                   "взрыв эмоций"],
    "u1F6A5.png": ["🚥", "светофор", "дорога", "правила", "остановка", "движение", "трафик", "регулирование",
                   "предупреждение", "путь"],
    "u1F47D.png": ["👽", "пришелец", "инопланетянин", "космос", "неизвестное", "фантастика", "внеземной",
                   "научная фантастика", "таинственное", "аномалия"],

}


def detect_faces(video_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(video_path)
    face_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        face_count = max(face_count, len(faces))

    cap.release()
    return face_count
def process_video_with_subtitles(videofilename,title,thumbnail_name, output_filename="output.mp4",new_subscription=None):
    current_directory = os.getcwd()
    print(current_directory,videofilename,os.path.exists(videofilename))
    if new_subscription==None:
        audiofilename = videofilename.replace(".mp4", ".mp3")
        input_stream = ffmpeg.input(videofilename)
        audio = input_stream.audio
        output_stream = ffmpeg.output(audio, audiofilename)
        output_stream = ffmpeg.overwrite_output(output_stream)
        ffmpeg.run(output_stream)

        model = whisper.load_model("medium")
        result = model.transcribe(audiofilename, word_timestamps=True)

        wordlevel_info = []
        for each in result['segments']:
            words = each['words']
            for word in words:
                wordlevel_info.append({
                    'word': word['word'].strip(),
                    'start': word['start'],
                    'end': word['end']
                })

    else:
        wordlevel_info=new_subscription


    subtitles_text = " ".join(
        word['word'].strip() for segment in result['segments'] for word in segment['words']
    )

    with open('data.json', 'w') as f:
        json.dump(wordlevel_info, f, indent=4)

    with open('data.json', 'r') as f:
        wordlevel_info_modified = json.load(f)

    linelevel_subtitles = split_text_into_lines(wordlevel_info_modified)

    input_video = VideoFileClip(videofilename)
    frame_size = input_video.size
    all_linelevel_splits = []

    for line in linelevel_subtitles:
        out = create_caption(line, frame_size,title=title)
        all_linelevel_splits.extend(out)

    final_video = CompositeVideoClip([input_video] + all_linelevel_splits)

    final_video = final_video.set_audio(input_video.audio)

    final_video.write_videofile(output_filename, fps=24, codec="libx264", audio_codec="aac")
    #first_frame_img = thumbnail_name
    #final_video.save_frame(first_frame_img, t=0)
    video_duration_seconds = final_video.duration


    video_duration_str = str(timedelta(seconds=video_duration_seconds))[
                         :-7]

    return [video_duration_str,wordlevel_info,subtitles_text]

def create_caption(textJSON, framesize, font="Roboto-Bold", fontsizee=23, color='white', bgcolor='blue',title=None):
    full_duration = textJSON['end'] - textJSON['start']
    fontsize=framesize[0]//20
    word_clips = []
    xy_textclips_positions = []

    x_pos = 100
    y_pos = 500
    frame_width = framesize[0]
    frame_height = framesize[1]
    x_buffer = frame_width * 1 / 40
    y_buffer = frame_height * 1 / 20

    if title:
        title_clip = TextClip(title, font=font, fontsize=fontsize * 2, color='black', bg_color='white')
        title_clip = title_clip.set_duration(2).set_position('center').resize(width=frame_width//2)
        word_clips.append(title_clip)

    for index, wordJSON in enumerate(textJSON['textcontents']):
        word = wordJSON['word'].lower()
        duration = wordJSON['end'] - wordJSON['start']
        word_clip = TextClip(wordJSON['word'], font=font, fontsize=fontsize, color=color).set_start(
            textJSON['start']).set_duration(full_duration)
        word_clip_space = TextClip(" ", font=font, fontsize=fontsize, color=color).set_start(
            textJSON['start']).set_duration(full_duration)
        word_width, word_height = word_clip.size
        space_width, space_height = word_clip_space.size
        if x_pos + word_width + space_width > frame_width - 2 * x_buffer:

            x_pos = 0
            y_pos = y_pos + word_height + 40


            xy_textclips_positions.append({
                "x_pos": x_pos + x_buffer,
                "y_pos": y_pos + y_buffer,
                "width": word_width,
                "height": word_height,
                "word": wordJSON['word'],
                "start": wordJSON['start'],
                "end": wordJSON['end'],
                "duration": duration
            })

            word_clip = word_clip.set_position((x_pos + x_buffer, y_pos + y_buffer))
            word_clip_space = word_clip_space.set_position((x_pos + word_width + x_buffer, y_pos + y_buffer))
            x_pos = word_width + space_width
        else:

            xy_textclips_positions.append({
                "x_pos": x_pos + x_buffer,
                "y_pos": y_pos + y_buffer,
                "width": word_width,
                "height": word_height,
                "word": wordJSON['word'],
                "start": wordJSON['start'],
                "end": wordJSON['end'],
                "duration": duration
            })

            word_clip = word_clip.set_position((x_pos + x_buffer, y_pos + y_buffer))
            word_clip_space = word_clip_space.set_position((x_pos + word_width + x_buffer, y_pos + y_buffer))

            x_pos = x_pos + word_width + space_width

        word_clips.append(word_clip)
        word_clips.append(word_clip_space)

        #print(f"Размер видео: {frame_width}x{frame_height}")

        for emodji, words_list in emoji.items():
            if word in words_list:
                #print("Эмодзи найдено:", emodji)
                try:

                    emoji_image_path = f"{emoji_image_folder}{emodji}"
                    #print(emoji_image_path)


                    emoji_clip = ImageClip(emoji_image_path).set_start(wordJSON['start']).set_duration(duration + 2).resize(0.4)

                    start_x = -emoji_clip.w  # Начальная позиция (за пределами экрана слева)
                    center_x = (frame_width - emoji_clip.w) / 2  # Центр экрана
                    end_x = frame_width  # Конечная позиция (за пределами экрана справа)


                    quick_move_duration = 0.1  # Время, за которое эмодзи перемещается в центр (в секундах)
                    stay_duration = 0.3 # Время, на которое эмодзи останется в центре (в секундах)
                    return_move_duration = 0.1  # Время, за которое эмодзи вернется обратно (в секундах)

                    # Общая продолжительность анимации
                    total_duration = quick_move_duration + stay_duration + return_move_duration

                    # Анимация: перемещение эмодзи
                    emoji_clip = emoji_clip.set_position(lambda t: (
                        start_x + (center_x - start_x) * (t / quick_move_duration) if t < quick_move_duration else
                        center_x if t < quick_move_duration + stay_duration else
                        center_x + (end_x - center_x) * (
                                    (t - (quick_move_duration + stay_duration)) / return_move_duration)
                        , 450))
                    emoji_clip = emoji_clip.set_duration(total_duration)

                    word_clips.append(emoji_clip)

                except Exception as e:
                    print(f"Ошибка создания эмодзи клипа: {e}")

    for highlight_word in xy_textclips_positions:
        word_clip_highlight = TextClip(highlight_word['word'], font=font, fontsize=fontsize, color=color,
                                       bg_color=bgcolor).set_start(highlight_word['start']).set_duration(
            highlight_word['duration'])
        word_clip_highlight = word_clip_highlight.set_position((highlight_word['x_pos'], highlight_word['y_pos']))
        word_clips.append(word_clip_highlight)

    return word_clips

def split_text_into_lines(data):
    MaxChars = 40
    MaxDuration = 0.5
    MaxGap = 0.3

    subtitles = []
    line = []
    line_duration = 0

    for idx, word_data in enumerate(data):
        start = word_data["start"]
        end = word_data["end"]

        line.append(word_data)
        line_duration += end - start

        temp = " ".join(item["word"] for item in line)
        new_line_chars = len(temp)
        duration_exceeded = line_duration > MaxDuration
        chars_exceeded = new_line_chars > MaxChars
        maxgap_exceeded = (idx > 0) and (word_data['start'] - data[idx - 1]['end'] > MaxGap)

        if duration_exceeded or chars_exceeded or maxgap_exceeded:
            if line:
                subtitle_line = {
                    "word": " ".join(item["word"] for item in line),
                    "start": line[0]["start"],
                    "end": line[-1]["end"],
                    "textcontents": line
                }
                subtitles.append(subtitle_line)
                line = []
                line_duration = 0

    if line:
        subtitle_line = {
            "word": " ".join(item["word"] for item in line),
            "start": line[0]["start"],
            "end": line[-1]["end"],
            "textcontents": line
        }
        subtitles.append(subtitle_line)

    return subtitles