import joblib
import pandas as pd

model = joblib.load("model.pkl")

def predict_url(url):

    length = len(url)
    has_login = 1 if "login" in url else 0
    has_https = 1 if "https" in url else 0

    df = pd.DataFrame([[length,has_login,has_https]],
                      columns=["length","has_login","has_https"])

    result = model.predict(df)[0]

    return "⚠ Phishing Risk" if result == 1 else "✅ Safe"