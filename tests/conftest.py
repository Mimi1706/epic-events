import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import *
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DB_URL")

@pytest.fixture(scope='function')
def mock_db_session():
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.begin()
    yield session 
    session.rollback()
    session.close() 


@pytest.fixture(scope='function')
def mock_employee(mock_db_session: Session):
    employee = Employee(
        email='jane@email.fr', 
        password='$2b$12$eb0YquWvV.QXxbmxbve4XePjFjOXm6/n0qL1tpB2vjFOKvRRFvV8W', 
        full_name='Jane Doe',
        department="gestion"
    )
    mock_db_session.add(employee)
    mock_db_session.commit()
    yield employee
    mock_db_session.flush()


@pytest.fixture(scope='function')
def mock_client(mock_db_session: Session):
    client = Client(
            company_name="Bloom",
            full_name="Iris Robinson",
            email="iris@email.com",
            phone_number="0657437628",
            sales_employee_id="1",
            created_on=datetime.now(),
            updated_on=datetime.now(),
        )
    mock_db_session.add(client)
    mock_db_session.commit()
    yield client


@pytest.fixture(scope='function')
def mock_contract(mock_db_session: Session):
    contract = Contract(
            client_id=0,
            status="pending",
            total_amount=300,
            left_amount=300,
            sales_employee_id=1,
            management_employee_id=1,
            created_on=datetime.now(),
            )
    mock_db_session.add(contract)
    mock_db_session.commit()
    yield contract


@pytest.fixture(scope='function')
def mock_event(mock_db_session: Session):
    event = Event(
            name="Flower class",
            start_date=datetime.now(),
            end_date=datetime.now(),
            location="Paris",
            attendees=25,
            notes="Attendees must bring their own furniture",
            management_employee_id=1,
            support_employee_id=1,
            )
    mock_db_session.add(event)
    mock_db_session.commit()
    yield event
