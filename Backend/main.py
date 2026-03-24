from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

from ai_model import predict_url

app = FastAPI()

# CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------- USERS --------
users = {}

@app.post("/signup")
def signup(data: dict):
    users[data["email"]] = data["password"]
    return {"msg": "User created"}

@app.post("/login")
def login(data: dict):
    if users.get(data["email"]) == data["password"]:
        return {"msg": "Login successful"}
    return {"error": "Invalid credentials"}

# -------- AI PHISHING --------
@app.post("/scan-url")
def scan_url(data: dict):
    result = predict_url(data["url"])
    return {"result": result}

# -------- EMAIL BREACH --------
@app.post("/check-email")
def check_email(data: dict):

    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{data['email']}"
    headers = {"user-agent":"cybershield"}

    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        return {"result": "⚠ Breached"}

    return {"result": "✅ Safe"}

# -------- AI ASSISTANT --------
@app.post("/ai")
def ai(data: dict):

    q = data["question"].lower()

    if "phishing" in q:
        return {"answer": "Avoid clicking fake login links."}

    if "password" in q:
        return {"answer": "Use strong passwords + 2FA."}

    return {"answer": "Stay safe online."}

# -------- SECURITY SCORE --------
@app.post("/score")
def score(data: dict):

    score = 100

    if "Phishing" in data["phishing"]:
        score -= 30

    if "Breached" in data["breach"]:
        score -= 40

    return {"score": score}