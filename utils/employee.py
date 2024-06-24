from utils.token import retrieve_payload_session
from database import session
from models import Employee
from permissions import EMPLOYEE_PERMISSIONS, CLIENT_PERMISSIONS, CONTRACT_PERMISSIONS, EVENT_PERMISSIONS
import os
import random
import string

SECRET_KEY = os.getenv("SECRET_KEY")

PERMISSIONS_MAP = {
    "EMPLOYEE": EMPLOYEE_PERMISSIONS,
    "CLIENT": CLIENT_PERMISSIONS,
    "CONTRACT": CONTRACT_PERMISSIONS,
    "EVENT": EVENT_PERMISSIONS,
}

def retrieve_employee_from_token():
    payload = retrieve_payload_session()
    employee: Employee = (
        session.query(Employee).filter(Employee.id == payload["id"]).first()
    )
    return employee


def check_permissions(permission_type):
    employee: Employee = retrieve_employee_from_token()
    role_permissions = PERMISSIONS_MAP.get(permission_type, {}).get(employee.department, {})
    allowed_actions = [
        action for action, allowed in role_permissions.items() if allowed
    ]
    return allowed_actions

def generate_password():
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(7))
    return password