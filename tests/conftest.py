import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import *
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DB_URL")


@pytest.fixture(scope="module")
def mock_db_session():
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.begin()
    yield session
    session.rollback()
    session.close()


@pytest.fixture(scope="module")
def mock_employee(mock_db_session: Session):
    employee = Employee(
        email="jane@email.fr",
        password="$2b$12$eb0YquWvV.QXxbmxbve4XePjFjOXm6/n0qL1tpB2vjFOKvRRFvV8W",
        full_name="Jane Doe",
        department="gestion",
    )
    mock_db_session.add(employee)
    mock_db_session.commit()
    yield employee
    mock_db_session.query(Client).filter(
        Client.sales_employee_id == employee.id
    ).delete()
    mock_db_session.delete(employee)
    mock_db_session.commit()
    mock_db_session.rollback()


@pytest.fixture(scope="module")
def mock_client(mock_db_session: Session, mock_employee: Employee):
    client = Client(
        company_name="Bloom",
        full_name="Iris Robinson",
        email="iris@email.com",
        phone_number="0657437628",
        sales_employee_id=mock_employee.id,
        created_on=datetime.now(),
        updated_on=datetime.now(),
    )
    mock_db_session.add(client)
    mock_db_session.commit()
    yield client
    mock_db_session.query(Contract).filter(Contract.client_id == client.id).delete()
    mock_db_session.delete(client)
    mock_db_session.commit()
    mock_db_session.rollback()


@pytest.fixture(scope="module")
def mock_contract(
    mock_db_session: Session,
    mock_employee: Employee,
    mock_client: Client,
):
    contract = Contract(
        created_on=datetime.now(),
        status="en attente",
        total_amount=300,
        left_amount=300,
        sales_employee_id=mock_employee.id,
        management_employee_id=mock_employee.id,
        client_id=mock_client.id,
    )
    mock_db_session.add(contract)
    mock_db_session.commit()
    yield contract
    mock_db_session.query(Event).filter(Event.contract_id == contract.id).delete()
    mock_db_session.delete(contract)
    mock_db_session.commit()
    mock_db_session.rollback()


@pytest.fixture(scope="module")
def mock_event(
    mock_db_session: Session,
    mock_employee: Employee,
    mock_contract: Contract,
):
    event = Event(
        name="Cours d'arrangement floral",
        start_date=datetime.now(),
        end_date=datetime.now(),
        location="Paris",
        attendees=25,
        notes="Les participants doivent amener leur propre matériel",
        contract_id=mock_contract.id,
        management_employee_id=mock_employee.id,
        support_employee_id=mock_employee.id,
    )
    mock_db_session.add(event)
    mock_db_session.commit()
    yield event
    mock_db_session.delete(event)
    mock_db_session.commit()
    mock_db_session.rollback()
