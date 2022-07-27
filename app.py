from flask import Flask

app = Flask(__name__)

@app.get("/welcome")
def say_welcome():
    """A welcoming message"""

    return "welcome"

@app.get("/welcome/home")
def say_welcome_home():
    """Welcome home message"""
    
    return "welcome home"


@app.get("/welcome/back")
def say_welcome_back():
    """Welcome back message"""
    return "welcome back"
