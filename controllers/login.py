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
        username = self.view.get_username()
        password = self.view.get_password().encode('utf-8')
        employee = session.query(Employee).filter(Employee.email == username).first()

        if employee:
            employee_password = employee.password.encode('utf-8')  
            if bcrypt.checkpw(password, employee_password):
                token = self.generate_jwt(employee)
                return token
        return None
    
    def generate_jwt(self, employee:Employee):
        payload = {
        'id': employee.id,
        'token_expiration': (datetime.now() + timedelta(hours=8)).isoformat()
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
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