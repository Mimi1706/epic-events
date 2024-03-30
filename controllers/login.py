from views.login import LoginView
from database import session
from models import Employee

class Login:
    def __init__(self):
        self.view = LoginView()

    def display_menu(self):
        username = self.view.get_username()
        password = self.view.get_password() 
        employee = session.query(Employee).filter(Employee.email == username).first()

        print(employee)