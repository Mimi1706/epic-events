from views.main_menu import MainMenuView
from controllers.login import Login
from controllers.employee import EmployeeController

class MainMenuController:
    def __init__(self):
        self.view = MainMenuView()

    def unlogged_menu(self):
        while True:
            user_input = self.view.unlogged_user_choice()
            if user_input == "1":
                employee = Login().log_in()
                if employee:
                    self.logged_menu(employee)
                else:
                    self.view.failed_login_msg()
            elif user_input == "2":
                self.view.goodbye_msg()
                quit()
            else:
                self.view.selection_error_msg()

    def logged_menu(self, employee):
        employee_controller = EmployeeController()
        while True:
            user_input = self.view.logged_user_choice(employee)
            if user_input == "1":
                employee_controller.display_menu(employee)
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