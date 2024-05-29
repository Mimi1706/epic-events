from pytest_mock import MockerFixture
from models.contract import Contract
from models.client import Client
from controllers.contract import ContractController
from sqlalchemy.orm import Session
from datetime import datetime
from io import StringIO


def test_create_contract(mocker: MockerFixture, mock_client:Client):
    contract_data = Contract(
        client_id=mock_client.id,
        status="2",
        total_amount=400,
        left_amount=400,
        sales_employee_id=1,
        management_employee_id=1,
        created_on=datetime.now(),
    )
    mocker.patch('builtins.input', side_effect= [
        contract_data.client_id,
        contract_data.status,
        contract_data.total_amount,
        contract_data.left_amount,
        contract_data.sales_employee_id,
        contract_data.management_employee_id,
        contract_data.created_on
    ])
    mock_print = StringIO()
    mocker.patch('sys.stdout', new=mock_print)
    ContractController().create_contract()
    assert mock_print.getvalue().strip() == "Contrat créé !"


# def test_delete_contract(mocker: MockerFixture, mock_contract:Contract):
#     print(mock_contract.id)
#     mocker.patch('builtins.input', side_effect= [ mock_contract.id, "1" ])
#     mock_print = StringIO()
#     mocker.patch('sys.stdout', new=mock_print)
#     ContractController().delete_contract()
#     assert mock_print.getvalue().strip() == "Contrat supprimé !"
