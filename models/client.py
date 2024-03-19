from sqlalchemy import Column, Date, Integer, String
from base import Base

class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    company_name = Column(String)
    created_on = Column(Date)
    updated_on = Column(Date)
    sales_employee_id = Column(String)