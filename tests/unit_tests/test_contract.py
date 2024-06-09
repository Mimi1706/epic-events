from pytest_mock import MockerFixture
from models.contract import Contract
from models.client import Client
from models.employee import Employee
from controllers.contract import ContractController
from datetime import datetime
from io import StringIO


def test_create_contract(
    mocker: MockerFixture, mock_client: Client, mock_employee: Employee
):
    contract_data = Contract(
        client_id=mock_client.id,
        total_amount=400,
        left_amount=400,
        sales_employee_id=mock_employee.id,
        management_employee_id=mock_employee.id,
        status="2",
        created_on=datetime.now(),
    )
    mocker.patch(
        "builtins.input",
        side_effect=[
            contract_data.client_id,
            contract_data.total_amount,
            contract_data.left_amount,
            contract_data.sales_employee_id,
            contract_data.management_employee_id,
            contract_data.status,
            contract_data.created_on,
        ],
    )
    mock_print = StringIO()
    mocker.patch("sys.stdout", new=mock_print)
    ContractController().create_contract()
    assert mock_print.getvalue().strip() == "Contrat créé !"


def test_find_contract(mocker: MockerFixture, mock_contract: Contract):
    mocker.patch("builtins.input", return_value=mock_contract.id)
    found_contract = ContractController().find_contract()
    assert found_contract is not None
    assert found_contract.id == mock_contract.id


def test_update_contract(mocker: MockerFixture, mock_contract: Contract):
    mocker.patch(
        "builtins.input",
        side_effect=[
            mock_contract.id,
            mock_contract.client_id,
            mock_contract.total_amount,
            mock_contract.left_amount,
            mock_contract.sales_employee_id,
            mock_contract.management_employee_id,
            "3",
        ],
    )
    mock_print = StringIO()
    mocker.patch("sys.stdout", new=mock_print)
    ContractController().update_contract()
    print_lines = mock_print.getvalue().strip().splitlines()
    assert print_lines[-1] == "Contrat mis à jour !"


def test_delete_contract(mocker: MockerFixture, mock_contract: Contract):
    mocker.patch("builtins.input", side_effect=[mock_contract.id, "1"])
    mock_print = StringIO()
    mocker.patch("sys.stdout", new=mock_print)
    ContractController().delete_contract()
    print_lines = mock_print.getvalue().strip().splitlines()
    assert print_lines[-1] == "Contrat supprimé !"
