from models.employee import Employee
from pytest_mock import MockerFixture
from controllers.employee import EmployeeController
from sqlalchemy.orm import Session

def test_find_employee(mock_employee:Employee, mocker: MockerFixture):
    mocker.patch('builtins.input', return_value=mock_employee.id)
    find_employee = EmployeeController().find_employee()
    assert find_employee is not None
    assert find_employee.id == mock_employee.id
    assert find_employee.full_name == mock_employee.full_name
    assert find_employee.email == mock_employee.email
    assert find_employee.department == mock_employee.department


def test_create_employee(mock_db_session:Session, mocker: MockerFixture):
    employee_data=Employee(
        full_name="Joshua Bryant",
        email="joshua@email.fr",
        department="1",
    )

    mocker.patch('builtins.input', side_effect= [
        employee_data.full_name,
        employee_data.email,
        employee_data.department,
    ])

    EmployeeController().create_employee()
    created_employee = mock_db_session.query(Employee).filter(Employee.email == employee_data.email).first()
    assert created_employee is not None
    assert created_employee.full_name == employee_data.full_name
    assert created_employee.email == employee_data.email


def test_update_employee(mock_db_session:Session, mocker: MockerFixture):
    created_employee = mock_db_session.query(Employee).filter(Employee.full_name == "Joshua Bryant").first()

    updated_employee_data=Employee(
        full_name="Charlotte Spencer",
        email="charlotte@email.fr"
    )

    mocker.patch('builtins.input', side_effect= [
        created_employee.id,
        updated_employee_data.full_name,
        updated_employee_data.email,
    ])

    EmployeeController().update_employee()
    updated_employee = mock_db_session.query(Employee).filter(Employee.id == created_employee.id).first()
    assert updated_employee.id == created_employee.id
    assert updated_employee.full_name is not "Joshua Bryant"


def test_delete_employee(mock_db_session:Session, mocker: MockerFixture):
    updated_employee = mock_db_session.query(Employee).filter(Employee.full_name == "Charlotte Spencer").first()
    mocker.patch('builtins.input', side_effect= [ updated_employee.id, "1" ])
    EmployeeController().delete_employee()
    mocker.patch('builtins.input', return_value=updated_employee.id)
    deleted_employee = EmployeeController().find_employee()
    assert deleted_employee is None