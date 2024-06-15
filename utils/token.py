from datetime import datetime, timedelta
from models import Employee
from views.login import LoginView
import jwt
import os
from datetime import datetime
from database import session

SECRET_KEY = os.getenv("SECRET_KEY")
TOKEN_FILE_PATH = "token.txt"

login_view = LoginView()


def check_token_expiration(token_date):
    given_date = datetime.fromisoformat(token_date)
    current_date = datetime.now()
    if given_date > current_date:
        return True
    return False

def generate_jwt(employee: Employee):
    payload = {
        "id": employee.id,
        "token_expiration": (datetime.now() + timedelta(hours=8)).isoformat(),
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    save_token(token)
    return token


def retrieve_payload_session():
    token = load_token()
    if token:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            employee: Employee = (session.query(Employee).filter(Employee.id == payload["id"]).first())
            if payload and check_token_expiration(payload.token_expiration) and employee:
                return payload
        except:
            login_view.error_msg()
            delete_token()
            quit()
    return None


def save_token(token):
    encoded_token = token.encode("utf-8")
    with open(TOKEN_FILE_PATH, "wb") as file:
        file.write(encoded_token)


def load_token():
    try:
        with open(TOKEN_FILE_PATH, "rb") as file:
            encoded_token = file.read()
            if not encoded_token:
                login_view.expired_session_msg()
                return None
            return encoded_token.decode("utf-8")
    except FileNotFoundError:
        pass


def delete_token():
    try:
        with open(TOKEN_FILE_PATH, "w"):
            pass
    except FileNotFoundError:
        pass
