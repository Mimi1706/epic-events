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

def retrieve_payload_session():
    try:
        token = load_token()
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        if datetime.now() > datetime.fromisoformat(payload["token_expiration"]):
            return LoginView.expired_session_msg()
        if payload:
            return payload
    except:
        LoginView.error_msg()
        delete_token()
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

def delete_token():
    file_path = "token.txt"
    try:
        with open(file_path, "w") as file: 
            pass
    except FileNotFoundError:
        pass