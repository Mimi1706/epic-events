from views.employee import EmployeeView
from models import Employee
from typing import List
from database import session
from utils.employee import check_permissions
import bcrypt


class EmployeeController:
    def __init__(self):
        self.view = EmployeeView()

    def display_menu(self):
        allowed_actions = check_permissions()
        while True:
            user_input = self.view.display_menu()
            if user_input == "1" and "READ" in allowed_actions:
                self.read_employees()
            elif user_input == "2" and "READ" in allowed_actions:
                self.find_employee()
            elif user_input == "3" and "CREATE" in allowed_actions:
                self.create_employee()
            elif user_input == "4" and "UPDATE" in allowed_actions:
                self.update_employee()
            elif user_input == "5" and "DELETE" in allowed_actions:
                self.delete_employee()
            elif user_input == "6":
                break

    def read_employees(self):
        employees: List[Employee] = session.query(Employee).all()
        sorted_employees: List[Employee] = sorted(
            employees, key=lambda employee: employee.department
        )
        self.view.display_employee_header()
        for employee in sorted_employees:
            self.view.display_employee(employee)

    def find_employee(self):
        user_input = self.view.find_employee()
        employee = session.query(Employee).filter(Employee.id == user_input).first()
        if employee:
            self.view.display_employee_header()
            self.view.display_employee(employee)
            return employee
        else:
            self.view.employee_not_found()

    def create_employee(self):
        full_name, email, department = self.view.edit_employee()
        if department not in {"1", "2", "3"} or not full_name or not email:
            self.view.create_employee_error()
        else:
            department = self.get_department_from_input(department)
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw("123".encode("utf-8"), salt)
            employee = Employee(
                full_name=full_name,
                department=department,
                email=email,
                password=hashed_password,
            )
            session.add(employee)
            session.commit()
            self.view.create_employee_success()

    def get_department_from_input(self, input_value):
        departments = {"1": "commercial", "2": "support", "3": "gestion"}
        return departments[input_value]

    def delete_employee(self):
        employee = self.find_employee()
        if employee:
            confirm_input = self.view.delete_employee_confirm()
            if confirm_input == "1":
                session.delete(employee)
                session.commit()
                self.view.delete_employee_success()

    def update_employee(self):
        employee = self.find_employee()
        if employee:
            full_name, email = self.view.edit_employee(ask_department=False)
            if not full_name or not email:
                self.view.update_employee_error()
            else:
                employee.full_name = full_name
                employee.email = email
                session.commit()
                self.view.update_employee_success()
