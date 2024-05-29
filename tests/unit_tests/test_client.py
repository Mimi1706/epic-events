from pytest_mock import MockerFixture
from models.client import Client
from controllers.client import ClientController
from sqlalchemy.orm import Session
from datetime import datetime

def test_create_client(mock_db_session:Session, mocker: MockerFixture):
    client = Client(
            company_name="Hello",
            full_name="Steven Johnson",
            email="steven@email.com",
            phone_number="0658745362",
            sales_employee_id="1",
            created_on=datetime.now(),
            updated_on=datetime.now(),
        )
    
    mocker.patch('builtins.input', side_effect=[ 
        client.company_name,
        client.full_name,
        client.email,
        client.phone_number,
        client.sales_employee_id,
        client.created_on,
        client.updated_on
     ])
    
    ClientController().create_client()
    created_client = mock_db_session.query(Client).filter(Client.company_name == client.company_name).first()
    assert created_client is not None
    assert created_client.full_name == client.full_name

def test_find_employee(mock_db_session:Session, mocker:MockerFixture):
    client = mock_db_session.query(Client).filter(Client.company_name == "Hello").first()
    mocker.patch('builtins.input', return_value=client.id)
    found_client = ClientController().find_client()
    assert found_client is not None
    assert found_client.full_name == "Steven Johnson"

def test_update_client(mock_db_session:Session, mocker:MockerFixture):
    found_client = mock_db_session.query(Client).filter(Client.company_name == "Hello").first()
    updated_client = Client(
        company_name="Goodbye",
        full_name="Steve Johnson",
        email="steve@email.com",
        phone_number="0658745352",
        sales_employee_id="1",
    )
    mocker.patch('builtins.input', side_effect= [
        found_client.id,
        updated_client.company_name,
        updated_client.full_name,
        updated_client.email,
        updated_client.phone_number,
        updated_client.sales_employee_id
    ])
    ClientController().update_client()
    mocker.patch('builtins.input', return_value=found_client.id)
    found_updated_client = ClientController().find_client()
    assert found_updated_client.company_name == "Goodbye"

def test_delete_client(mock_db_session:Session, mocker:MockerFixture):
    found_client = mock_db_session.query(Client).filter(Client.company_name == "Goodbye").first()
    mocker.patch('builtins.input', side_effect=[found_client.id, "1"])
    ClientController().delete_client()
    mocker.patch('builtins.input', return_value=found_client.id)
    found_deleted_client = ClientController().find_client()
    assert found_deleted_client is None

