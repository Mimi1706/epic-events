from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(length=255))
    email = Column(String(length=255))
    phone_number = Column(String(length=15))
    company_name = Column(String(length=255))
    created_on = Column(Date)
    updated_on = Column(Date)
    sales_employee_id = Column(String(length=255))

    sales_employee = relationship("Employee", foreign_keys=[sales_employee_id], back_populates="clients")
