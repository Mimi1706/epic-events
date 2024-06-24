from pytest_mock import MockerFixture
from models.client import Client
from models.employee import Employee
from controllers.client import ClientController
from datetime import datetime
from io import StringIO


def test_create_client(mocker: MockerFixture, mock_employee: Employee):
    client_data = Client(
        company_name="HelloTest",
        full_name="Steven Johnson",
        email="steven@email.com",
        phone_number="0658745362",
        sales_employee_id=mock_employee.id,
        created_on=datetime.now(),
        updated_on=datetime.now(),
    )
    mocker.patch(
        "builtins.input",
        side_effect=[
            client_data.company_name,
            client_data.full_name,
            client_data.email,
            client_data.phone_number,
            client_data.sales_employee_id,
            client_data.created_on,
            client_data.updated_on,
        ],
    )
    mock_print = StringIO()
    mocker.patch("sys.stdout", new=mock_print)
    ClientController().create_client()
    print_lines = mock_print.getvalue().strip().splitlines()
    assert print_lines[-1] == "Client créé !"


def test_find_client(mocker: MockerFixture, mock_client: Client):
    mocker.patch("builtins.input", return_value=mock_client.id)
    found_client = ClientController().find_client()
    assert found_client is not None
    assert found_client.id == mock_client.id
    assert found_client.full_name == mock_client.full_name
    assert found_client.company_name == mock_client.company_name


def test_update_client(
    mocker: MockerFixture, mock_employee: Employee, mock_client: Client
):
    updated_client = Client(
        company_name="GoodbyeTest",
        full_name="Steve Johnson",
        email="steve@email.com",
        phone_number="0658745352",
        sales_employee_id=mock_employee.id,
    )
    mocker.patch(
        "builtins.input",
        side_effect=[
            mock_client.id,
            updated_client.company_name,
            updated_client.full_name,
            updated_client.email,
            updated_client.phone_number,
            updated_client.sales_employee_id,
        ],
    )
    mock_print = StringIO()
    mocker.patch("sys.stdout", new=mock_print)
    ClientController().update_client()
    print_lines = mock_print.getvalue().strip().splitlines()
    assert print_lines[-1] == "Client mis à jour !"


def test_delete_client(mocker: MockerFixture, mock_client: Client):
    mocker.patch("builtins.input", side_effect=[mock_client.id, "1"])
    mock_print = StringIO()
    mocker.patch("sys.stdout", new=mock_print)
    ClientController().delete_client()
    print_lines = mock_print.getvalue().strip().splitlines()
    assert print_lines[-1] == "Client supprimé !"
