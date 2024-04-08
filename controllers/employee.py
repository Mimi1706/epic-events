from views.employee import EmployeeView
from models import Employee
from typing import List
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
                self.find_employee()
            elif user_input == "3" and 'CREATE' in allowed_actions:
                print('création autorisée')
            elif user_input == "4" and 'UPDATE' in allowed_actions:
                print('modification autorisée')
            elif user_input == "5" and 'DELETE' in allowed_actions:
                print('suppression autorisée')
            elif user_input == "6":
                quit()

    def read_employees(self):
        employees: List[Employee] = session.query(Employee).all()
        sorted_employees: List[Employee] = sorted(employees, key=lambda employee:employee.department)
        self.view.display_employee_header()
        for employee in sorted_employees:
            self.view.display_employee(employee)

    def find_employee(self):
        user_input = self.view.find_employee()
        employee = session.query(Employee).filter(Employee.id == user_input).first()
        if employee:
            self.view.display_employee_header()
            return self.view.display_employee(employee)
        else:
            return self.view.employee_not_found()