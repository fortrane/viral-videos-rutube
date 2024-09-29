import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AdamW
from datasets import Dataset
from torch.utils.data import DataLoader
from tqdm import tqdm
from datasets.tag_dataset import train_data  # Выбираем датасет

tokenizer = AutoTokenizer.from_pretrained("cointegrated/rut5-base-multitask")
model = AutoModelForSeq2SeqLM.from_pretrained("cointegrated/rut5-base-multitask")


def tokenize_data(examples):
    inputs = examples['input_text']  # Получаем список входных текстов
    targets = examples['target_text']  # Получаем список целевых тегов

    # Токенизируем входные данные (тексты)
    model_inputs = tokenizer(inputs, max_length=512, truncation=True, padding="max_length")

    # Токенизируем цели (теги)
    with tokenizer.as_target_tokenizer():
        labels = tokenizer(targets, max_length=128, truncation=True, padding="max_length")

    model_inputs["labels"] = labels["input_ids"]
    return model_inputs


# Подготовка данных для обучения
train_dataset = Dataset.from_list(train_data)
train_dataset = train_dataset.map(tokenize_data, batched=True)


# Функция collate_fn для преобразования данных в тензоры
def collate_fn(batch):
    input_ids = torch.tensor([item['input_ids'] for item in batch], dtype=torch.long)
    attention_mask = torch.tensor([item['attention_mask'] for item in batch], dtype=torch.long)
    labels = torch.tensor([item['labels'] for item in batch], dtype=torch.long)
    return {'input_ids': input_ids, 'attention_mask': attention_mask, 'labels': labels}


train_dataloader = DataLoader(train_dataset, batch_size=8, shuffle=True, collate_fn=collate_fn)

# Настройка модели и оптимизатора
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

optimizer = AdamW(model.parameters(), lr=5e-5)

model.train()
num_epochs = 100

for epoch in range(num_epochs):
    progress_bar = tqdm(train_dataloader, desc=f"Epoch {epoch + 1}")
    for batch in progress_bar:
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['labels'].to(device)

        # Прямой проход
        outputs = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss

        # Обратный проход
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        progress_bar.set_postfix(loss=loss.item())


def generate_tags(text: str, max_length: int = 15) -> str:
    input_text = f"Сформулируй теги для текста: {text}"
    input_ids = tokenizer.encode(input_text, return_tensors="pt", truncation=True, max_length=512).to(device)

    output = model.generate(input_ids, max_length=max_length, num_beams=5, temperature=1, num_return_sequences=1)

    result = tokenizer.decode(output[0], skip_special_tokens=True)
    return result


# Тестик)
text = "Этот текст рассказывает о новых технологиях и гаджетах."
tags = generate_tags(text)
print(f"Сгенерированные теги: {tags}")

# Сохранение модели
model.save_pretrained("./tag_generation_model")
tokenizer.save_pretrained("./tag_generation_model")
