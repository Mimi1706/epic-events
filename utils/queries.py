from models import Employee, Client
from database import session


def get_employee(employee_id):
    employee: Employee = (
    session.query(Employee).filter(Employee.id == employee_id).first()
    )
    return employee if employee is not None else None

def get_client(client_id):
    client: Client = (
    session.query(Client).filter(Client.id == client_id).first()
    )
    return client if client is not None else None