import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load dataset
data = pd.read_csv("scam_dataset.csv")

X = data["text"]
y = data["label"]

# Convert text to numbers
vectorizer = CountVectorizer()
X_vector = vectorizer.fit_transform(X)

# Train model
model = MultinomialNB()
model.fit(X_vector, y)

def predict_scam(message):
    msg_vector = vectorizer.transform([message])
    prediction = model.predict(msg_vector)[0]
    
    if prediction == 1:
        return "⚠️ Scam Detected"
    else:
        return "✅ Safe Message"
