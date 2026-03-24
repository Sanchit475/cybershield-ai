import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Dummy dataset (you can replace later)
data = pd.DataFrame({
    "length":[10,50,100,200,300,500],
    "has_login":[1,1,1,0,0,0],
    "has_https":[0,0,1,1,1,1],
    "label":[1,1,1,0,0,0]  # 1 = phishing
})

X = data[["length","has_login","has_https"]]
y = data["label"]

model = RandomForestClassifier()
model.fit(X,y)

joblib.dump(model,"model.pkl")

print("Model trained!")