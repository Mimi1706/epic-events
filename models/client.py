from sqlalchemy import Column, Date, Integer, String, ForeignKey
from .base import Base


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(length=255))
    email = Column(String(length=255))
    phone_number = Column(String(length=15))
    company_name = Column(String(length=255))
    created_on = Column(Date)
    updated_on = Column(Date)
    sales_employee_id = Column(Integer, ForeignKey("employees.id"))
