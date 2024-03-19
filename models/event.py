from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    location = Column(String)
    attendees = Column(Integer)
    notes = Column(String)
    support_employee_id = Column(String)
    management_employee_id = Column(String)
    contrat_id = Column(Integer, ForeignKey('contrats.id'))
    contrat = relationship("Contract", back_populates="events")