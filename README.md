# Email Spam Classifier

This is a Python-based email spam classification project that uses machine learning algorithms to classify emails as spam or not spam. It uses a Support Vector Machine model along with TF-IDF for feature extraction to perform the classification. The web interface is built using Flask, and it allows users to input email content and classify it.

## Table of Contents
- [Project Description](#project-description)
- [Technologies Used](#technologies-used)
- [Installation](#installation)

## Project Description

This project classifies emails as spam or not spam using a pre-trained Logistic Regression model and TF-IDF (Term Frequency-Inverse Document Frequency) vectorization. Users can enter the email content through a web interface (Flask), and the system will display whether the email is spam or not.

### Features:
- Email content input via a user-friendly web interface.
- Spam classification using machine learning.
- Result display in a clear, color-coded format (Spam or Not Spam).

## Technologies Used

- Python 3.x
- Flask (Web Framework)
- Scikit-learn (Machine Learning Library)
- NLTK (Natural Language Toolkit for text processing)
- Pandas (Data processing)
- Matplotlib (Data visualization)
- Seaborn (Visualization Library)

## Installation

To get this project up and running, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Keshav-Kant/EmailSpam.git
   cd EmailSpam
