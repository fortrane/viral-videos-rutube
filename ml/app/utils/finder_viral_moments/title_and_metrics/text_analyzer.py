# -*- coding: utf-8 -*-
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = T5Tokenizer.from_pretrained("cointegrated/rut5-base-multitask", legacy=False)
model = T5ForConditionalGeneration.from_pretrained("cointegrated/rut5-base-multitask").to(device)

# Генерим тайтл
def generate_chunk_title(chunk: str) -> str:
    input_text = f"Сформулируй вопросительное название отображающее смысл текста: {chunk}"
    input_ids = tokenizer.encode(input_text, return_tensors="pt").to(device)
    output = model.generate(input_ids, max_length=50, num_return_sequences=1, temperature=1)

    result = tokenizer.decode(output[0], skip_special_tokens=True)
    return result

