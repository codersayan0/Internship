# GPT-2 Fine-Tuning on Custom Text

This project fine-tunes **GPT-2** using the Hugging Face `transformers` library on a **custom text dataset**. It works even with small datasets and is designed for beginners experimenting with text generation.

---

## Features
- Fine-tunes GPT-2 on any plain text file (`train.txt`).
- Supports **tiny datasets** (even with just a few lines).
- Uses **block size truncation (default: 32)** for efficient training.
- Saves both **model & tokenizer** for future text generation.

---

## Project Structure
```
project/
│
├── data/
│   └── train.txt        # Your custom text dataset
│
├── gpt2-finetuned/      # Output directory for fine-tuned model
│
├── Text_Generation.py   # Main training script
└── README.md            # This file
```

---

## Requirements
- Python 3.8+
- Install dependencies:
```bash
pip install transformers datasets torch
```

---

## How to Use

### 1. Prepare Your Dataset
Create a file:
```
data/train.txt
```
Add your training text, for example:
```
Once upon a time there was a kind king.
He ruled the kingdom with wisdom and love.
People admired his fairness and courage.
```

### 2. Run Training
```bash
python Text_Generation.py
```

The script will:
- Load GPT-2 & tokenizer
- Tokenize your text
- Fine-tune the model
- Save the trained model to `gpt2-finetuned/`

### 3. Generate Text (Example)
After training, use this quick script to generate text:
```python
from transformers import GPT2LMHeadModel, GPT2TokenizerFast

model_path = "./gpt2-finetuned"
tokenizer = GPT2TokenizerFast.from_pretrained(model_path)
model = GPT2LMHeadModel.from_pretrained(model_path)

prompt = "Once upon a time"
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_length=50, num_return_sequences=1)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

---

## Configuration
Key parameters (edit in `Text_Generation.py`):
- `BLOCK_SIZE = 32` → Context window size for splitting text.
- `EPOCHS = 3` → Number of training epochs.
- `BATCH_SIZE = 2` → Batch size for training.
- `DATA_PATH = "./data/train.txt"` → Training file location.
- `OUTPUT_DIR = "./gpt2-finetuned"` → Where to save the model.

---

## Notes
- With **very small datasets**, the model may overfit quickly.
- For **better results**, provide at least **50+ lines** of text.
- Fine-tuning GPT-2 on larger datasets may require a GPU.

---

## License
This project is for **educational purposes only**. Based on [Hugging Face Transformers](https://github.com/huggingface/transformers).
