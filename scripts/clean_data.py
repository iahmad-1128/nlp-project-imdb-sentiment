
import pandas as pd
import unicodedata
import re
import nltk

from pathlib import Path
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet


# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "IMDB Dataset.csv"
OUTPUT_FILE = BASE_DIR / "data" / "cleaned_imdb_dataset.csv"


# Download required NLTK resources
nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)
nltk.download("omw-1.4", quiet=True)


# Load dataset
df = pd.read_csv(INPUT_FILE)

print("Original Dataset Shape:", df.shape)


# Stopwords (preserving negation words)
stop_words = set(stopwords.words("english"))

negation_words = {
    "no", "not", "nor", "don't", "didn't",
    "doesn't", "isn't", "wasn't", "weren't",
    "won't", "wouldn't", "couldn't", "shouldn't",
    "can't", "cannot"
}

stop_words = stop_words - negation_words

lemmatizer = WordNetLemmatizer()


# Cleaning function
def clean_text(text):

    # Unicode normalization
    text = unicodedata.normalize("NFKC", text)

    # Lowercase
    text = text.lower()

    # Remove HTML tags
    text = re.sub(r"<[^>]+>", "", text)

    # Remove URLs
    text = re.sub(r"https?://\S+|www\.\S+", "", text)

    # Remove unwanted special characters
    text = re.sub(r"[^\w\s'!?]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    # Remove stopwords while preserving negation
    words = text.split()
    words = [word for word in words if word not in stop_words]

    # Lemmatization
    words = [
        lemmatizer.lemmatize(word, wordnet.VERB)
        for word in words
    ]

    return " ".join(words)


# Apply cleaning to all reviews
df["cleaned_review"] = df["review"].apply(clean_text)


# Vocabulary before cleaning
original_words = set()

for review in df["review"]:
    original_words.update(review.lower().split())


# Vocabulary after cleaning
cleaned_words = set()

for review in df["cleaned_review"]:
    cleaned_words.update(review.split())


# Display results
print("\nVocabulary Before Cleaning:", len(original_words))
print("Vocabulary After Cleaning:", len(cleaned_words))
print("Vocabulary Reduction:", len(original_words) - len(cleaned_words))


# Save cleaned dataset
df[["cleaned_review", "sentiment"]].to_csv(
    OUTPUT_FILE,
    index=False
)

print("\nCleaned dataset saved successfully!")
print("Output:", OUTPUT_FILE)
