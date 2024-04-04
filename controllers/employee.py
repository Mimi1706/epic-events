from views.employee import EmployeeView
from models import Employee
from database import session
from permissions import EMPLOYEE_PERMISSIONS

class EmployeeController:
    def __init__(self):
        self.view = EmployeeView()

    def display_menu(self, employee:Employee):
        role_permissions = EMPLOYEE_PERMISSIONS.get(employee.department, {})
        allowed_actions = [action for action, allowed in role_permissions.items() if allowed]

        while True:
            user_input = self.view.display_menu(employee)
            if user_input == "1" and 'READ' in allowed_actions:
                self.read_employees()
            elif user_input == "2" and 'READ' in allowed_actions:
                print('recherche autorisée')
            elif user_input == "3" and 'CREATE' in allowed_actions:
                print('création autorisée')
            elif user_input == "4" and 'UPDATE' in allowed_actions:
                print('modification autorisée')
            elif user_input == "5" and 'DELETE' in allowed_actions:
                print('suppression autorisée')
            elif user_input == "6":
                quit()

    def read_employees(self):
        employees = session.query(Employee).all()
        print("\nID | Name")
        print("-------------------")
        for employee in employees:
            print(f"{employee.id}  | {employee.full_name}")