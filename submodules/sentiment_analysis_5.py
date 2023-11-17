import os
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import numpy as np
from scipy.special import softmax
import csv
import urllib.request

articles_to_analyze = [
    '1755_Lisbon_earthquake.txt',
    '1896_Summer_Olympics.txt',
    '1997_Pacific_hurricane_season.txt',
    'Actinium.txt',
    'Barracuda.txt',
    'Basketball.txt',
    'Bath_School_disaster.txt',
    'Chicago.txt',
    'Chocolate.txt',
    'Diamond.txt',
    'Dice.txt',
    'Drinking_water.txt',
    'Duchenne_muscular_dystrophy.txt',
    'Geography_of_Ireland.txt',
    'George_S_Richardson_engineer.txt',
    'Giraffe.txt',
    'Gunpowder.txt',
    'Ordinal_number.txt',
    'Osama_bin_Laden.txt',
    'Palm_oil.txt',
    'Peace.txt',
    'Pellagra.txt',
    'Phishing.txt',
    'Plant.txt',
    'Plato.txt',
    'Pneumonia.txt',
    'Poison_gas_in_World_War_I.txt',
    'Politics.txt',
    'Pollution.txt',
    'Pompeii.txt',
    'Recycling.txt',
    'Red_Kite.txt',
    'Rice.txt',
    'Rio_de_Janeiro.txt',
    'Robert_K_Beck.txt',
    'Romeo_and_Juliet.txt',
    'Rugby_World_Cup.txt',
    'Rwandan_Genocide.txt',
    'Salt.txt',
    'Sand.txt',
    'Santa_Claus.txt',
    'Scooby-Doo.txt',
    'Seed.txt',
    'Sequoia.txt'
]


# Function to preprocess the text
def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)

# Function to chunk text into manageable parts
def chunk_text(text, max_length):
    words = text.split()
    for i in range(0, len(words), max_length):
        yield ' '.join(words[i:i+max_length])

# Function to adjust score with the lexicon
def adjust_score_with_lexicon(text, score, positive_words, negative_words, max_adjustment=0.5):
    words = text.split()
    positive_count = sum(word in positive_words for word in words)
    negative_count = sum(word in negative_words for word in words)

    if abs(score) >= 0.2:
        difference = positive_count - negative_count
        adjustment = (np.log(abs(difference) + 1) / np.log(max_adjustment + 1)) * np.sign(difference)
        adjustment = np.clip(adjustment, -max_adjustment, max_adjustment)
    else:
        return score

    score += adjustment
    score = np.clip(score, -1, 1)
    return score


if __name__ == "__main__":
    zip_file_path = '../data/plaintext_articles.zip'
    content_dir = '../data/plaintext_articles'

    text_files = [os.path.join(content_dir, file) for file in articles_to_analyze]

    for file_path in text_files:
        print("Analyzing file: ", file_path)

        with open(file_path, 'r') as file:
            text = file.read()

        # Define the task and model
        task = 'sentiment'
        MODEL = f"cardiffnlp/twitter-roberta-base-{task}"

        print("Loading tokenizer...")

        # Load tokenizer and model from Hugging Face
        tokenizer = AutoTokenizer.from_pretrained(MODEL)
        print("Loading sequence classification model...")
        model = AutoModelForSequenceClassification.from_pretrained(MODEL, num_labels=3, finetuning_task=task)

        # Set the max_length for tokenization
        max_length = 512

        # Download and load the label mapping
        labels = []
        mapping_link = f"https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/{task}/mapping.txt"
        print("Loading label mapping...")
        # with urllib.request.urlopen(mapping_link) as f:
        #     print("in file")
        #     html = f.read().decode('utf-8').split("\n")
        #     print("decoded")
        #     csvreader = csv.reader(html, delimiter='\t')
        #     print("read")
        # labels = [row[1] for row in csvreader if len(row) > 1]
        labels = ["negative", "neutral", "positive"]

        print("Loading pos-neg lexicons...")
        # Load positive and negative words lists (assuming you have them as text files)
        # positive_words = set(open('../data_posneg/positive-words.txt').read().splitlines())
        # negative_words = set(open('../data_posneg/negative-words.txt').read().splitlines())

        positive_words = set()
        negative_words = set()
        with open("../data_posneg/positive-words.txt", 'r') as file:
            for line in file.readlines():
                positive_words.add(line.strip())
        with open("../data_posneg/negative-words.txt", 'r') as file:
            for line in file.readlines():
                negative_words.add(line.strip())
        print("Loaded lexicons.")

        chunks = chunk_text(preprocess(text), max_length)
        final_scores = np.zeros(len(labels))
        for chunk in chunks:
            print("tokenizing...")
            encoded_input = tokenizer(chunk, return_tensors='pt', truncation=True, max_length=max_length)
            print("inferring...")
            output = model(**encoded_input)
            scores = softmax(output[0][0].detach().numpy())
            final_scores += scores


        final_scores /= final_scores.sum()

        sentiment_score = final_scores[2] - final_scores[0]  # Positive score minus negative score
        sentiment_score = adjust_score_with_lexicon(preprocess(text), sentiment_score, positive_words, negative_words)

        print(f"File: {os.path.basename(file_path)} - Sentiment score: {sentiment_score:.2f}")
        print("")