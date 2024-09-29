# -*- coding: utf-8 -*-
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch


tokenizer = AutoTokenizer.from_pretrained(r"C:\Users\Admin\PycharmProjects\pythonProject\viral_clips_hackton\app\utils\finder_viral_moments\tag_generation_model", legacy=False)
model = AutoModelForSeq2SeqLM.from_pretrained(r"C:\Users\Admin\PycharmProjects\pythonProject\viral_clips_hackton\app\utils\finder_viral_moments\tag_generation_model")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Генерим теги
def generate_tags(text: str, max_length: int = 15) -> str:
    input_text = f"Сформулируй теги для текста: {text}"
    input_ids = tokenizer.encode(input_text, return_tensors="pt", truncation=True, max_length=512).to(device)

    output = model.generate(input_ids, max_length=max_length, num_beams=5, temperature=1, num_return_sequences=1)

    result = tokenizer.decode(output[0], skip_special_tokens=True)
    return result
