# pip install nrclex
import spacy
from nltk.metrics import edit_distance
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from nrclex import NRCLex
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')


def analyze_emotions(text):
    emotion = NRCLex(text)
    return emotion.affect_frequencies


# Example usage
text = "Hi, I'm having a problem with my computer. The screen is completely blank and I can't see anything. Can you help me?"
emotion = analyze_emotions(text)

# Print the emotion and its score
for e, score in emotion.items():
    print(f"{e}: {score}")


def main():
    while True:
        text = input("customer: ")
        emotion = analyze_emotions(text)
        for e, score in emotion.items():
            print(f"{e}: {score}")
        answeable = input("agent: ")
        if answeable == "exit":
            break


main()


# Load data dictionary (assuming it's a dictionary with sentence as key and emotion score as value)
data_dict = {
    "I am happy.": 0.8,
    "I am sad.": 0.2,
    "you are useless": 0.1,
    "you are great": 0.9,
    "I am angry": 0.1,
    "I hate you": 0.1,
    "I love you": 0.9,
    "I am so happy": 0.9,
    "I am so sad": 0.1,
    "I am so angry": 0.1,
    "I am so useless": 0.1,

}

# Preprocess sentences (example using NLTK for tokenization and stopword removal)

# Load data dictionary (assuming it's a dictionary with sentence as key and emotion score as value)
data_dict = {
    "I am happy.": 0.8,
    "I am sad.": 0.2,
    # more sentences...
}


# Sample data

# Sample data

# Sample data

# Sample data

# Sample data
sentences = [
    "I am feeling happy",
    "I feel sad",
    "Feeling joyful",
    "I am not happy",
    "I am ecstatic"
]

# Sample emotion scores
emotion_scores = [0.8, 0.5, 0.9, 0.3, 0.7]

# Load spaCy's English language model
nlp = spacy.load("en_core_web_md")

# Calculate similarity scores
similarity_scores = []
for i, sentence in enumerate(sentences):
    doc1 = nlp(sentence)
    scores = []
    for j, other_sentence in enumerate(sentences):
        if i != j:  # Exclude self-comparison
            doc2 = nlp(other_sentence)
            scores.append(doc1.similarity(doc2))
    similarity_scores.append(scores)

# Sort sentences based on similarity scores and emotion scores
sorted_sentences = sorted(zip(
    sentences, similarity_scores, emotion_scores), key=lambda x: (-max(x[1]), x[2]))

# Print top 5 sentences with highest similarity scores and low emotion scores
for i in range(5):
    print("Sentence:", sorted_sentences[i][0])
    print("Similarity Score:", max(sorted_sentences[i][1]))
    print("Emotion Score:", sorted_sentences[i][2])
    print()
