from transformers import AutoModelForSequenceClassification, AutoTokenizer
import numpy as np
from scipy.special import softmax
import csv

def calculatesentiment(text):
    MODEL_DIR = "./sentiment_model"
    TOKENIZER_DIR = "./tokenizer"

    # Load labels from CSV
    labels = []
    try:
        with open("sentiment_labels.csv", newline='', encoding='utf-8') as file:
            csvreader = csv.reader(file)
            labels = [row[1] for row in csvreader if len(row) > 1]
    except FileNotFoundError:
        print("sentiment_labels.csv not found. Using default labels.")
        labels = ["negative", "neutral", "positive"]  # Default labels

    try:
        # Load tokenizer and model from local directories
        tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_DIR)
        model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR)

        # Tokenize input text
        encoded_input = tokenizer(text, return_tensors='pt', truncation=True, padding=True)

        # Get model outputs
        output = model(**encoded_input)
        scores = output.logits[0].detach().numpy()
        scores = softmax(scores)

        # Create a sorted ranking based on scores
        ranking = np.argsort(scores)[::-1]
        top_sentiment = labels[ranking[0]] if labels and ranking[0] < len(labels) else labels[1]  # Fallback to neutral if index out of range

        return labels, scores.tolist(), top_sentiment

    except Exception as e:
        print(f"Error in sentiment analysis: {str(e)}")
        return ["negative", "neutral", "positive"], [0.0, 0.0, 0.0], "neutral"  # Fallback to neutral on error