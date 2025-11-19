import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split

# Dataset must contain: "url", "label"
df = pd.read_csv("phishing_url_dataset.csv")

X = df["url"]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = make_pipeline(
    TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5)),
    RandomForestClassifier(n_estimators=200, random_state=42)
)

model.fit(X_train, y_train)

joblib.dump(model, "phishing_url_model.pkl")
print("Saved phishing_url_model.pkl")
