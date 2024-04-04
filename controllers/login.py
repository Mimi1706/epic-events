from views.login import LoginView
from database import session
from models import Employee
import bcrypt

import bcrypt

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
                return employee
            
        return None