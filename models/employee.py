from sqlalchemy import Column, Integer, String, CheckConstraint
from .base import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(length=255))
    department = Column(String(length=255))
    email = Column(String(length=255))
    password = Column(String(length=255))

    __table_args__ = (
        CheckConstraint(
            department.in_(["commercial", "support", "gestion"]),
            name="valid_department",
        ),
    )
