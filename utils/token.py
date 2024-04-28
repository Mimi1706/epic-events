from datetime import datetime, timedelta
from models import Employee
from views.login import LoginView
import jwt
import os

SECRET_KEY = os.getenv("SECRET_KEY")

def generate_jwt(employee:Employee):
    payload = {
    'id': employee.id,
    'token_expiration': (datetime.now() + timedelta(hours=8)).isoformat()
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    save_token(token)
    return token

def authorize_user(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        if datetime.now() > datetime.fromisoformat(payload["token_expiration"]):
            LoginView.expired_session_msg()
        else:
            if payload["id"]:
                return True
            return False
    except jwt.InvalidTokenError:
        LoginView.error_msg()
        quit()

def save_token(token):
    file_path = "token.txt"
    encoded_token = token.encode('utf-8') 
    with open(file_path, "wb") as file: 
        file.write(encoded_token)

def load_token():
    file_path = "token.txt"
    try:
        with open(file_path, "rb") as file: 
            encoded_token = file.read()
            return encoded_token.decode('utf-8')  
    except FileNotFoundError:
        pass
    return None

def validate_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        expiration = datetime.fromisoformat(payload['token_expiration'])
        if datetime.now() < expiration:
            return payload
        else:
            return None
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return False 