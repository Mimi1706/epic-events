from controllers.login import Login
from models.employee import Employee
from pytest_mock import MockerFixture

def test_login(generate_employee: Employee, mocker: MockerFixture):
    test_email = generate_employee.email
    mocker.patch('builtins.input', side_effect=[test_email, "1"])
    login = Login().log_in()
    assert login is not None
    assert login.full_name == "Jane Doe"