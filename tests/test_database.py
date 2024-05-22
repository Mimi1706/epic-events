from sqlalchemy.orm import sessionmaker
from models import Employee
from database import engine

Session = sessionmaker(bind=engine)
session = Session()

def test_retrieve_all_employees():
    employees = session.query(Employee).all()
    assert isinstance(employees, list)
    assert len(employees) == 2 
