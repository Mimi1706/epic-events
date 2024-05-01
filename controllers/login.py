from views.login import LoginView
from database import session
from models import Employee
from utils.token import generate_jwt
import bcrypt

class Login:
    def __init__(self):
        self.view = LoginView()

    def log_in(self):
        username = self.view.get_username()
        password = self.view.get_password().encode('utf-8')
        employee = session.query(Employee).filter(Employee.email == username).first()
        if employee and bcrypt.checkpw(password, employee.password.encode('utf-8')):
            generate_jwt(employee)
            return employee
        self.view.wrong_credentials_msg()
        return None

