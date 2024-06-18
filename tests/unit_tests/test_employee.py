from models.employee import Employee
from pytest_mock import MockerFixture
from controllers.employee import EmployeeController
from io import StringIO
from sqlalchemy.orm import Session


def test_find_employee(mock_employee: Employee, mocker: MockerFixture):
    mocker.patch("builtins.input", return_value=mock_employee.id)
    found_employee = EmployeeController().find_employee()
    assert found_employee is not None
    assert found_employee.id == mock_employee.id
    assert found_employee.full_name == mock_employee.full_name
    assert found_employee.email == mock_employee.email
    assert found_employee.department == mock_employee.department


def test_create_employee(mock_db_session: Session, mocker: MockerFixture):
    employee_data = Employee(
        full_name="Joshua Bryant",
        email="joshua@email.fr",
        department="1",
    )
    mocker.patch(
        "builtins.input",
        side_effect=[
            employee_data.full_name,
            employee_data.email,
            employee_data.department,
        ],
    )
    mock_print = StringIO()
    mocker.patch("sys.stdout", new=mock_print)
    EmployeeController().create_employee()
    print_lines = mock_print.getvalue().strip().splitlines()
    assert print_lines[0] == "Utilisateur créé !"
    mock_db_session.rollback()


def test_update_employee(mocker: MockerFixture, mock_employee: Employee):
    updated_employee_data = Employee(
        full_name="Charlotte Spencer", email="charlotte@email.fr"
    )
    mocker.patch(
        "builtins.input",
        side_effect=[
            mock_employee.id,
            updated_employee_data.full_name,
            updated_employee_data.email,
        ],
    )
    mock_print = StringIO()
    mocker.patch("sys.stdout", new=mock_print)
    EmployeeController().update_employee()
    print_lines = mock_print.getvalue().strip().splitlines()
    assert print_lines[-1] == "Utilisateur mis à jour !"


def test_delete_employee(mock_db_session: Session, mocker: MockerFixture):
    created_employee = (
        mock_db_session.query(Employee)
        .filter(Employee.full_name == "Joshua Bryant")
        .first()
    )
    mocker.patch("builtins.input", side_effect=[created_employee.id, "1"])
    mock_print = StringIO()
    mocker.patch("sys.stdout", new=mock_print)
    EmployeeController().delete_employee()
    print_lines = mock_print.getvalue().strip().splitlines()
    assert print_lines[-1] == "Utilisateur supprimé !"
