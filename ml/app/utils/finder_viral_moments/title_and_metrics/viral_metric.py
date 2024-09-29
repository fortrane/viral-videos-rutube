# -*- coding: utf-8 -*-
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration
from .viral_count_params import params

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-large", legacy=False)
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-large").to(device)


def chunk_text(text: str, max_tokens=450) -> list:
    sentences = text.split('. ')
    chunks = []
    current_chunk = []
    current_length = 0

    for sentence in sentences:
        tokenized_sentence = tokenizer.encode(sentence, return_tensors="pt").to(device)
        token_length = tokenized_sentence.shape[1]

        if current_length + token_length > max_tokens:
            # Если добавление текущего предложения превышает лимит, добавим текущий чанк в список
            chunks.append(' '.join(current_chunk))
            current_chunk = [sentence]  # начинаем новый чанк
            current_length = token_length
        else:
            current_chunk.append(sentence)
            current_length += token_length

    # Добавим последний чанк, если он не пустой
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks


# Получаем оценку по одному параметру
def evaluate_parameter(param: str, text: str) -> dict:
    input_text = f"{param} {text}"
    input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True).to(device)
    output = model.generate(input_ids, max_length=15, num_return_sequences=1)
    result = tokenizer.decode(output[0], skip_special_tokens=True)
    return result


# Получение оценки по каждому параметру
def evaluate_chunk(chunk: str) -> list:
    results = {}
    for param in params:
        score = evaluate_parameter(param, text=chunk)
        results[param] = score

    chunk_score = []
    for r_param, r_score in results.items():

        chunk_score.append([r_param, r_score])

    return chunk_score


# Оцениваем весь текст по чанкам
def evaluate_text(text: str, max_tokens: int) -> list:
    chunks = chunk_text(text, max_tokens=max_tokens)
    text_res = []
    for chunk in chunks:
        chun_res = {}
        chunk_score = evaluate_chunk(chunk)
        chun_res["chunk"] = chunk
        chun_res["chunk_score"] = chunk_score
        text_res.append(chun_res)

    return text_res
