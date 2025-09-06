# text_generation_gpt2.py
# Fine-tuning GPT-2 on a custom text file (works even with small datasets)

import os
from datasets import load_dataset
from transformers import (
    GPT2LMHeadModel,
    GPT2TokenizerFast,
    DataCollatorForLanguageModeling,
    Trainer,
    TrainingArguments,
)

# ==============================
# 1. Configuration
# ==============================
MODEL_NAME = "gpt2"
DATA_PATH = "./data/train.txt"      # Make sure this file exists
OUTPUT_DIR = "./gpt2-finetuned"     # Output directory for the model
BLOCK_SIZE = 32                     # Lower block size for small datasets
EPOCHS = 3
BATCH_SIZE = 2

# ==============================
# 2. Load tokenizer & model
# ==============================
tokenizer = GPT2TokenizerFast.from_pretrained(MODEL_NAME)
tokenizer.pad_token = tokenizer.eos_token  # Avoid pad token error
model = GPT2LMHeadModel.from_pretrained(MODEL_NAME)

# ==============================
# 3. Load dataset
# ==============================
if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"Training file not found at {DATA_PATH}")

dataset = load_dataset("text", data_files={"train": DATA_PATH})

# ==============================
# 4. Tokenize
# ==============================
def tokenize_function(examples):
    return tokenizer(examples["text"], truncation=True)

tokenized = dataset.map(tokenize_function, batched=True)

# ==============================
# 5. Handle small datasets
# ==============================
# 5. Handle small datasets
def group_texts(examples):
    # Flatten all input_ids from this batch
    all_ids = []
    for ids in examples["input_ids"]:
        all_ids.extend(ids)

    # If dataset has no tokens
    if len(all_ids) == 0:
        return {"input_ids": [], "labels": []}

    # If dataset is too small, just return one padded sample
    if len(all_ids) < BLOCK_SIZE:
        padded = all_ids + [tokenizer.eos_token_id] * (BLOCK_SIZE - len(all_ids))
        return {"input_ids": [padded], "labels": [padded]}

    # Normal chunking for larger datasets
    total_length = (len(all_ids) // BLOCK_SIZE) * BLOCK_SIZE
    all_ids = all_ids[:total_length]
    chunks = [all_ids[i:i + BLOCK_SIZE] for i in range(0, total_length, BLOCK_SIZE)]
    return {"input_ids": chunks, "labels": chunks}

# Map safely
lm_datasets = tokenized.map(group_texts, batched=True, remove_columns=tokenized["train"].column_names)


# ==============================
# 6. Data collator
# ==============================
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False,
)

# ==============================
# 7. Training arguments
# ==============================
training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    overwrite_output_dir=True,
    num_train_epochs=EPOCHS,
    per_device_train_batch_size=BATCH_SIZE,
    save_steps=200,
    save_total_limit=1,
    logging_dir="./logs",
    logging_steps=10,
)

# ==============================
# 8. Trainer
# ==============================
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=lm_datasets["train"],
    data_collator=data_collator,
)

# ==============================
# 9. Train
# ==============================
trainer.train()

# ==============================
# 10. Save model & tokenizer
# ==============================
trainer.save_model(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)
print(f"Model saved to {OUTPUT_DIR}")
