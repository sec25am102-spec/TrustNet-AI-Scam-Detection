import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("scam_dataset.csv")

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['text'])

model = LogisticRegression()
model.fit(X, data['label'])

def predict_scam(message):
    msg = vectorizer.transform([message])
    prediction = model.predict(msg)[0]
    
    if prediction == 1:
        return "⚠️ Scam Detected"
    else:
        return "✅ Safe Message"
