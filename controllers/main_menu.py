from views.main_menu import MainMenuView
from controllers.login import Login
from controllers.employee import EmployeeController
from controllers.client import ClientController
from database import session
from models import Employee
from utils.token import authorize_user
import os
import jwt

class MainMenuController:
    def __init__(self):
        self.view = MainMenuView()

    def unlogged_menu(self):
        while True:
            user_input = self.view.unlogged_user_choice()
            if user_input == "1":
                token = Login().log_in()
                if token:
                    self.logged_menu(token)
                else:
                    self.view.failed_login_msg()
            elif user_input == "2":
                self.view.goodbye_msg()
                quit()
            else:
                self.view.selection_error_msg()

    def logged_menu(self, token):
        employee = self.retrieve_employee(token)
        while True:
            authorize_user(token)
            user_input = self.view.logged_user_choice(employee.full_name)
            if user_input == "1":
                EmployeeController().display_menu(employee)
            elif user_input == "2":
                pass
            elif user_input == "3":
                pass
            elif user_input == "4":
                pass
            elif user_input == "5":
                self.view.goodbye_msg()
                quit()
            else:
                self.view.selection_error_msg()

    def retrieve_employee(self, token):
        SECRET_KEY = os.getenv("SECRET_KEY")
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        employee: Employee = session.query(Employee).filter_by(id=payload["id"]).first()
        if not employee:
            self.view.unauthorized_msg()
            quit()
        return employee