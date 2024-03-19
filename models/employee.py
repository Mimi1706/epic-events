from sqlalchemy import Column, Integer, String,CheckConstraint
from base import Base

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    department = Column(String)

    __table_args__ = (
        CheckConstraint(department.in_(['sales', 'support', 'management']), name='valid_department'),
    )