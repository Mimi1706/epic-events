from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=255))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    location = Column(String(length=255))
    attendees = Column(Integer)
    notes = Column(String(length=255))
    support_employee_id = Column(String(length=255))
    management_employee_id = Column(String(length=255))
    contrat_id = Column(Integer, ForeignKey('contracts.id'))
    contrat = relationship("Contract", back_populates="events")