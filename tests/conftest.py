import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models.base import Base  
from models.employee import Employee  
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DB_URL")

@pytest.fixture(scope='module')
def db_engine():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

@pytest.fixture(scope='function')
def db_session(db_engine):
    Session = sessionmaker(bind=db_engine)
    session = Session()
    yield session
    session.close()

@pytest.fixture(scope='function')
def generate_employee(db_session: Session):
    employee = Employee(
        email='jane@email.fr', 
        password='$2b$12$eb0YquWvV.QXxbmxbve4XePjFjOXm6/n0qL1tpB2vjFOKvRRFvV8W', 
        full_name='Jane Doe',
        department="gestion"
    )
    db_session.add(employee)
    db_session.commit()
    yield employee
    db_session.rollback()
