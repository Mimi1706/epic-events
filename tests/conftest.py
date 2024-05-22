import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models.employee import Employee  
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
