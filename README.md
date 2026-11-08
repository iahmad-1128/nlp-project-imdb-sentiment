# IMDb Movie Reviews Sentiment Analysis

## 1. Project Overview

This project focuses on Sentiment Analysis of IMDb movie reviews using Natural Language Processing (NLP).

The objective is to process movie reviews and prepare textual data for sentiment classification by identifying whether a review expresses a positive or negative opinion.

## 2. Dataset

We use the IMDb 50K Movie Reviews Dataset.

- Total reviews: 50,000
- Positive reviews: 25,000
- Negative reviews: 25,000
- Columns: `review`, `sentiment`

The original dataset should be placed inside the `data/` folder with the filename:

`IMDB Dataset.csv`

## 3. Project Structure

```text
nlp-project-imdb-sentiment/
│
├── data/
│   ├── IMDB Dataset.csv
│   └── cleaned_imdb_dataset.csv
│
├── notebooks/
│   ├── exploration_tokenization.ipynb
│   └── text_cleaning.ipynb
│
├── requirements.txt
├── README.md
└── .gitignore
```

## 4. Project Tasks

### Member 1: Dataset Exploration and Tokenization

- Loaded and explored the IMDb dataset.
- Analyzed the distribution of positive and negative reviews.
- Examined examples of messy text.
- Performed tokenization using NLTK and regular expressions.
- Explored tokenization challenges.

### Member 2: Text Preprocessing and Cleaning

- Applied Unicode normalization.
- Converted text to lowercase.
- Removed HTML tags, URLs, and unnecessary special characters.
- Removed stopwords while preserving negation words.
- Applied lemmatization.
- Created a reusable `clean_text()` function.
- Compared vocabulary size before and after cleaning.
- Generated a cleaned dataset.

## 5. Installation and Setup

Clone the repository:

```bash
git clone https://github.com/iahmad-1128/nlp-project-imdb-sentiment.git
```

Move into the project directory:

```bash
cd nlp-project-imdb-sentiment
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it in Windows PowerShell:

```powershell
.venv\Scripts\Activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## 6. Running the Project

Open the project folder in VS Code or Jupyter Notebook.

Run the notebooks in this order:

1. `exploration_tokenization.ipynb`
2. `text_cleaning.ipynb`

Make sure the original IMDb dataset is available inside the `data/` folder before running the notebooks.

## 7. Output

The preprocessing notebook generates:

`data/cleaned_imdb_dataset.csv`

This file contains cleaned movie reviews and their corresponding sentiment labels.

## 8. Technologies and Libraries

- Python
- Jupyter Notebook
- Pandas
- NumPy
- NLTK
- Regular Expressions (Regex)
- spaCy
- Matplotlib
- Git and GitHub