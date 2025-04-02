# Import libraries
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from hmmlearn.hmm import GaussianHMM
import numpy as np

# Load dataset
data = fetch_20newsgroups(categories=['comp.graphics', 'sci.med'], remove=('headers', 'footers', 'quotes'))
labels = [0 if target == 0 else 1 for target in data.target]  # Ensure labels are correctly mapped

# Preprocess data
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data.data).toarray()

# Train HMM to extract features
hmm = GaussianHMM(n_components=3, covariance_type="diag", n_iter=100)
hmm.fit(X)  # Fit the HMM on the entire dataset
features = hmm.predict(X).reshape(-1, 1)  # Predict to get sequence features

# Train Naive Bayes on HMM features
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
nb_model = GaussianNB()
nb_model.fit(X_train, y_train)

# Test hybrid model
preds = nb_model.predict(X_test)
print("Hybrid model accuracy:", accuracy_score(y_test, preds))