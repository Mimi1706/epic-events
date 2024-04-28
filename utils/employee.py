from utils.token import retrieve_payload_session
from database import session
from models import Employee
from permissions import EMPLOYEE_PERMISSIONS
import os

SECRET_KEY = os.getenv("SECRET_KEY")

def retrieve_employee_from_token():
    payload = retrieve_payload_session()
    employee:Employee = session.query(Employee).filter(Employee.id == payload["id"]).first()
    return employee 
    
def check_permissions():
    employee:Employee = retrieve_employee_from_token()
    role_permissions = EMPLOYEE_PERMISSIONS.get(employee.department, {})
    allowed_actions = [action for action, allowed in role_permissions.items() if allowed]
    return allowed_actions