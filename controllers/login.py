from views.login import LoginView
from database import session
from models import Employee
import bcrypt
from datetime import datetime, timedelta
import jwt
import os

SECRET_KEY = os.getenv("SECRET_KEY")

class Login:
    def __init__(self):
        self.view = LoginView()

    def log_in(self):
        token = self.load_token()
        payload = self.validate_token(token)
        if token and payload:
            employee = session.query(Employee).filter(Employee.id == payload["id"]).first()
            if employee:
                return self.generate_jwt(employee)
            
        username = self.view.get_username()
        password = self.view.get_password().encode('utf-8')
        employee = session.query(Employee).filter(Employee.email == username).first()
        if employee and bcrypt.checkpw(password, employee.password.encode('utf-8')):
            return self.generate_jwt(employee)

        return None

    
    def generate_jwt(self, employee:Employee):
        payload = {
        'id': employee.id,
        'token_expiration': (datetime.now() + timedelta(hours=8)).isoformat()
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        self.save_token(token)
        return token
    
    def authorize_user(self, token):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            if datetime.now() > datetime.fromisoformat(payload["token_expiration"]):
                self.view.expired_session_msg()
            else:
                if payload["id"]:
                    return True
                return False
        except jwt.InvalidTokenError:
            self.view.error_msg()
            quit()

    def save_token(self, token):
        file_path = "token.txt"
        encoded_token = token.encode('utf-8') 
        with open(file_path, "wb") as file: 
            file.write(encoded_token)

    def load_token(self):
        file_path = "token.txt"
        try:
            with open(file_path, "rb") as file: 
                encoded_token = file.read()
                return encoded_token.decode('utf-8')  
        except FileNotFoundError:
            pass
        return None

    def validate_token(self, token):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            expiration = datetime.fromisoformat(payload['token_expiration'])
            if datetime.now() < expiration:
                return payload
            else:
                return None
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            return False 