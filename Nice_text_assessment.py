#pip install nrclex
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

from nrclex import NRCLex


def analyze_emotions(text):
    emotion = NRCLex(text)
    return emotion.affect_frequencies


# Example usage
text = Hi, I'm having a problem with my computer. The screen is completely blank and I can't see anything. Can you help me?
emotion = analyze_emotions(text)

# Print the emotion and its score
for e, score in emotion.items():
    print(f"{e}: {score}")


