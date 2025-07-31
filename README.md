<!-- PROJECT TITLE -->
<h1 align="center">🎬 Movie Reviews Sentiment Analysis Web App 🎭</h1>

---

<!-- PROJECT DESCRIPTION -->
## 📌 Project Description
This project is a Flask-based web application that performs sentiment analysis on movie reviews using Natural Language Processing (NLP) and machine learning techniques. The core of the model is based on Naive Bayes classifiers (MultinomialNB, BernoulliNB, and GaussianNB), and it uses a custom-trained vectorizer on the IMDB dataset. 

Users can input their movie reviews through the web interface, and the model will predict whether the review sentiment is **positive** or **negative**.

---

<!-- FEATURES -->
## ✨ Features
- Clean and responsive front-end with Bootstrap styling.
- Real-time sentiment prediction using a trained model.
- Preprocessing steps including tokenization, stopword removal, and stemming.
- Supports multiple Naive Bayes models for comparison.
- Displays prediction results instantly.

---

<!-- TECH STACK -->
## 🛠️ Tech Stack
- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Python, Flask
- **ML/NLP**: Scikit-learn, NLTK, Pandas, NumPy
- **Model**: Naive Bayes Classifiers (MultinomialNB, BernoulliNB, GaussianNB)

---

<!-- DATASET -->
## 📊 Dataset
- **Source**: IMDB Movie Reviews Dataset (~50,000 labeled reviews)
- **Features**:
  - `review`: The text content of the movie review.
  - `sentiment`: The label (`positive` or `negative`) indicating the sentiment of the review.

> ⚠️ Note: The dataset is large (~63MB) and may exceed GitHub's file size limit. Consider using Git Large File Storage (LFS) if needed: https://git-lfs.github.com

---

