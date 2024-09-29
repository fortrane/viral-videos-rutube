# -*- coding: utf-8 -*-

from faster_whisper import WhisperModel
import re


def seconds_to_hms(seconds):  # Подтягивает время
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return f"{int(hours):02d}:{int(minutes):02d}:{seconds:.2f}"


# Получаем текст и таймстепы
def audio_to_text(audio):
    model_size = "small"
    # Run on GPU with FP16
    model = WhisperModel(model_size, device="cuda", compute_type="float16")

    # or run on GPU with INT8
    # model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
    # or run on CPU with INT8
    # model = WhisperModel(model_size, device="cpu", compute_type="int8")

    segments, info = model.transcribe(audio, beam_size=5, language='ru', word_timestamps=False)

    # file_result = open('../txt_res.txt', 'w', encoding='utf-8')

    txt_result = []
    onl_txt = []
    for segment in segments:
        start_time = seconds_to_hms(float(segment.start))
        end_time = seconds_to_hms(float(segment.end))
        text = segment.text
        onl_txt.append(text)
        timestamp_seg = [f'{start_time} - {end_time}', text]
        txt_result.append(timestamp_seg)

    # file_result.write(str(txt_result))

    combined_text = ''.join(onl_txt)

    #print(txt_result, combined_text)
    return {'with_ts': txt_result, 'only_t': combined_text}


# Находим начало и конец отрывка
def find_time_range(timestamps: list, search_text: str) -> list:
    start_time = None
    end_time = None
    search_words = re.findall(r'\w+', search_text.lower())  # Поиск только слов
    word_index = 0

    for time_range, text in timestamps:
        words = re.findall(r'\w+', text.lower())  # Нормализация текста в нижний регистр и поиск только слов
        for word in words:
            if word == search_words[word_index]:
                if start_time is None:
                    start_time = time_range.split(' - ')[0]
                word_index += 1
                if word_index == len(search_words):
                    end_time = time_range.split(' - ')[1]
                    return [start_time, end_time]
            else:
                start_time = None
                word_index = 0

    return [start_time, end_time]
