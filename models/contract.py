from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from .base import Base

class Contract(Base):
    __tablename__ = 'contracts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_on = Column(Date)
    status = Column(String(length=255))
    total_amount = Column(Float)
    left_amount = Column(Float)
    sales_employee_id = Column(Integer, ForeignKey('employees.id'))
    management_employee_id = Column(Integer, ForeignKey('employees.id'))
    client_id = Column(Integer, ForeignKey('clients.id'))

    sales_employee = relationship("Employee", foreign_keys=[sales_employee_id], back_populates="contracts")
    management_employee = relationship("Employee", foreign_keys=[management_employee_id], back_populates="contracts")
    client = relationship("Client", foreign_keys=[client_id], back_populates="contracts")
    
    __table_args__ = (
        CheckConstraint(status.in_(['signed', 'pending', 'cancelled']), name='valid_status'),
    )