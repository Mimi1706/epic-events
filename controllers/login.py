from views.login import LoginView
from database import session
from models import Employee
from utils.token import generate_jwt, load_token, retrieve_payload_session
import bcrypt

class Login:
    def __init__(self):
        self.view = LoginView()

    def log_in(self):
        token = load_token()
        payload = retrieve_payload_session()
        if token and payload:
            employee = session.query(Employee).filter(Employee.id == payload["id"]).first()
            if employee:
                return generate_jwt(employee)
        username = self.view.get_username()
        password = self.view.get_password().encode('utf-8')
        employee = session.query(Employee).filter(Employee.email == username).first()
        if employee and bcrypt.checkpw(password, employee.password.encode('utf-8')):
            return generate_jwt(employee)
        return None
