
# 📊 Sentiment Analysis Web App

A lightweight and interactive **Streamlit-based sentiment analysis app** that classifies input text into **Positive**, **Neutral**, or **Negative** sentiments using a locally stored pre-trained transformer model.

---

## 🧩 Project Structure

```
SENTIMENT_ANALYSIS_PROJECT/
├── __pycache__/
│   └── sentiment.cpython-313.pyc         # Compiled Python cache
├── sentiment_model/
│   ├── config.json                       # Model configuration
│   └── model.safetensors                 # Pre-trained model weights
├── tokenizer/
│   ├── merges.txt
│   ├── special_tokens_map.json
│   ├── tokenizer_config.json
│   ├── tokenizer.json
│   └── vocab.json
├── app.py                                # Main Streamlit app
├── sentiment.py                          # Sentiment analysis logic
├── sentiment_labels.csv                  # Optional sentiment labels
└── Sentiment graph.pdf                   # Visualization (optional)
```

---

## 🚀 Overview

- **Purpose:** Analyze sentiment of input text in real-time with emoji and chart feedback.
- **Sentiments Detected:** `Positive`, `Neutral`, `Negative`
- **Tech Stack:** `Python`, `Streamlit`, `Transformers`, `PyTorch`, `Matplotlib`
- **Model & Tokenizer:** Loaded locally from `sentiment_model/` and `tokenizer/` directories.

---

## ⚙️ Installation Guide

### ✅ Prerequisites
- Python ≥ 3.7
- Git

### 📥 Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Shimu-I/sentiment_analysis_project.git
   cd sentiment_analysis_project
   ```

2. **Create and Activate Virtual Environment (Optional)**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Create `requirements.txt`**
   ```txt
   streamlit
   matplotlib
   transformers
   scipy
   torch
   numpy
   ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ How to Use

### Start the App
```bash
streamlit run app.py
```

- Open your browser: [http://localhost:8501](http://localhost:8501)

### Interact with It
- Enter your text (e.g., `"I love this app!"`)
- Click **Predict**
- View:
  - Emoji for top sentiment
  - Bar chart with sentiment score breakdown

---

## 🧪 Sample Inputs

| Sentiment | Examples |
|----------|----------|
| 😊 Positive | I feel great! <br> Sun shines brightly! |
| 😐 Neutral | Weather is normal. <br> Meeting starts soon. |
| 😠 Negative | I feel awful. <br> Lost my keys. |

---

## 🧠 File & Feature Breakdown

### `app.py`
- UI and interaction logic using Streamlit
- Emoji feedback and bar chart (via Matplotlib)

### `sentiment.py`
- Loads model/tokenizer from local folders
- Computes softmax of logits for prediction
- Returns sentiment label, scores, and emoji

### `sentiment_model/`
- `model.safetensors`: Pre-trained model weights
- `config.json`: Hugging Face-compatible model config

### `tokenizer/`
- All tokenizer files (e.g., `vocab.json`, `tokenizer_config.json`) required to decode text

### `sentiment_labels.csv` *(Optional)*
- Defines output labels like:
  ```
  0,negative
  1,neutral
  2,positive
  ```

---

## 🔧 Customization

| Custom Feature | How to Modify |
|----------------|----------------|
| Input box height | Change in `st.markdown()` CSS in `app.py` |
| Emojis | Modify `emoji_mapping` in `app.py` |
| Sentiment labels | Retrain model and update `sentiment_labels.csv` |

---

## 🛠 Troubleshooting

| Issue | Solution |
|-------|----------|
| App won’t start | Check Streamlit install & command: `streamlit run app.py` |
| Model errors | Ensure `model.safetensors` and `config.json` exist in `sentiment_model/` |
| Tokenizer errors | Make sure all tokenizer files exist inside `tokenizer/` |
| Label mismatch | Ensure `sentiment_labels.csv` matches model output classes |

---


## 📦 Large File Handling (Git LFS Required)

This project uses **Git Large File Storage (LFS)** to manage the transformer model file (`model.safetensors`), which exceeds GitHub’s regular size limit.

### 🔧 Install Git LFS

Before cloning or pushing, make sure you have Git LFS installed:

```bash
# Windows, macOS, or Linux
git lfs install
```

### 📥 Clone with Git LFS Enabled

```bash
git clone https://github.com/Shimu-I/sentiment_analysis_project.git
cd sentiment_analysis_project
```

Git LFS will automatically download the large model files when you clone the repository.

### 🧩 Updated Project Structure

Update this part of your structure slightly to make clear the file is tracked with LFS:

```diff
├── sentiment_model/
│   ├── config.json                       # Model configuration
-│   └── model.safetensors                 # Pre-trained model weights
+│   └── model.safetensors (tracked via Git LFS) # Pre-trained model weights
```
