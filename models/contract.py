from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from base import Base

class Contract(Base):
    __tablename__ = 'contracts'

    id = Column(Integer, primary_key=True)
    created_on = Column(Date)
    status = Column(String)
    total_amount = Column(Float)
    left_amount = Column(Float)
    sales_employee_id = Column(String)
    management_employee_id = Column(String)
    client_id = Column(Integer, ForeignKey('clients.id'))
    client = relationship("Client", back_populates="contracts")

    __table_args__ = (
        CheckConstraint(status.in_(['signed', 'pending', 'cancelled']), name='valid_status'),
    )