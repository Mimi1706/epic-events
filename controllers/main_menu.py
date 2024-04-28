from views.main_menu import MainMenuView
from controllers.login import Login
from controllers.employee import EmployeeController
from controllers.client import ClientController
from utils.employee import retrieve_employee_from_token

class MainMenuController:
    def __init__(self):
        self.view = MainMenuView()

    def unlogged_menu(self):
        while True:
            user_input = self.view.unlogged_user_choice()
            if user_input == "1":
                token = Login().log_in()
                if token:
                    self.logged_menu()
                else:
                    self.view.failed_login_msg()
            elif user_input == "2":
                self.view.goodbye_msg()
                quit()
            else:
                self.view.selection_error_msg()

    def logged_menu(self):
        employee = retrieve_employee_from_token()
        while True:
            user_input = self.view.logged_user_choice(employee.full_name)
            if user_input == "1":
                EmployeeController().display_menu()
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
