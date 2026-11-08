# IMDb Movie Reviews Sentiment Analysis

## 1. Project Overview

This project focuses on Sentiment Analysis of IMDb movie reviews using Natural Language Processing (NLP).

The objective is to explore, tokenize, and clean movie reviews to prepare textual data for positive and negative sentiment classification.

## 2. Dataset

We use the **IMDb Dataset of 50K Movie Reviews**.

- Total reviews: 50,000
- Positive reviews: 25,000
- Negative reviews: 25,000
- Columns: `review`, `sentiment`
- Language: English

**Dataset source:**  
https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews

**Original research dataset:**  
Andrew L. Maas et al. (2011), *Learning Word Vectors for Sentiment Analysis*.  
https://ai.stanford.edu/~amaas/data/sentiment/

**Licence information:**  
The Kaggle dataset page lists its licence as "Other (specified in description)". Users should check the dataset page and its applicable terms before reusing or redistributing the data.

### Dataset Setup

The dataset is not stored in this GitHub repository because of its large file size.

1. Download the dataset from the Kaggle link above.
2. Extract the downloaded file.
3. Create a folder named `data` in the project root.
4. Place `IMDB Dataset.csv` inside the `data` folder.

The expected file path is:

`data/IMDB Dataset.csv`

## 3. Project Structure

```text
nlp-project-imdb-sentiment/
│
├── data/                         # Local datasets (not tracked by Git)
│   ├── IMDB Dataset.csv
│   └── cleaned_imdb_dataset.csv
│
├── notebooks/
│   ├── exploration_tokenization.ipynb
│   └── text_cleaning.ipynb
│
├── scripts/
│   ├── load_data.py
│   └── clean_data.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## 4. Project Tasks

### Member 1: Dataset Exploration and Tokenization

- Loaded and explored the IMDb dataset.
- Analyzed positive and negative sentiment distribution.
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
- Created reusable data-loading and cleaning scripts.

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

Download the IMDb dataset and place it inside the `data/` folder as explained in Section 2.

## 6. Running the Project

Run commands from the project root directory.

### Step 1: Load and Explore the Dataset

```bash
python scripts/load_data.py
```

This script displays:

- Dataset shape
- Column names
- First five records
- Missing values
- Sentiment distribution

### Step 2: Clean the Dataset

```bash
python scripts/clean_data.py
```

This script:

- Normalizes Unicode text.
- Converts reviews to lowercase.
- Removes HTML tags and URLs.
- Removes unnecessary special characters.
- Removes stopwords while preserving negation.
- Applies lemmatization.
- Calculates vocabulary reduction.
- Saves the cleaned dataset.

### Step 3: Run the Notebooks

Open the notebooks in Jupyter Notebook or VS Code and execute their cells.

Run them in this order:

1. `notebooks/exploration_tokenization.ipynb`
2. `notebooks/text_cleaning.ipynb`

Make sure the original dataset is available inside the `data/` folder.

## 7. Output

The cleaning script generates:

`data/cleaned_imdb_dataset.csv`

The output contains two columns:

- `cleaned_review`
- `sentiment`

The cleaned dataset contains 50,000 reviews.

## 8. Cleaning Results

| Metric | Result |
|---|---:|
| Vocabulary before cleaning | 390,931 |
| Vocabulary after cleaning | 131,728 |
| Vocabulary reduction | 259,203 |
| Reduction percentage | Approximately 66.3% |

## 9. Technologies and Libraries

- Python
- Jupyter Notebook
- Pandas
- NumPy
- NLTK
- Regular Expressions (Regex)
- spaCy
- Matplotlib
- Git and GitHub

## 10. Reproducibility

To reproduce the project:

1. Clone the GitHub repository.
2. Install the required packages.
3. Download and place the original dataset in the `data/` folder.
4. Run `python scripts/load_data.py`.
5. Run `python scripts/clean_data.py`.
6. Open and execute the exploration and cleaning notebooks.

GitHub Repository:  
https://github.com/iahmad-1128/nlp-project-imdb-sentiment

## 11. Academic Integrity and AI Assistance

AI assistance was used for guidance, debugging, and support during the development and documentation of the project. The team reviewed and tested the project code and is responsible for understanding the submitted work.

## 12. Team Members

- Member 1: Ahmad Iftikhar L1F23BSCS1128
- Member 2: Aiza Shafiq  L1F23BSCS1135
