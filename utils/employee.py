from utils.token import load_token, authorize_user
from database import session
from models import Employee
from permissions import EMPLOYEE_PERMISSIONS
import jwt
import os

SECRET_KEY = os.getenv("SECRET_KEY")

def retrieve_employee_from_token():
    token = load_token()
    if authorize_user(token):
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        employee = session.query(Employee).filter(Employee.id == payload["id"]).first()
        return employee
    
def check_permissions(employee_department): 
    role_permissions = EMPLOYEE_PERMISSIONS.get(employee_department, {})
    allowed_actions = [action for action, allowed in role_permissions.items() if allowed]
    return allowed_actions