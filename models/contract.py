from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, CheckConstraint
from .base import Base


class Contract(Base):
    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_on = Column(Date)
    status = Column(String(length=255))
    total_amount = Column(Float)
    left_amount = Column(Float)
    sales_employee_id = Column(Integer, ForeignKey("employees.id"))
    management_employee_id = Column(Integer, ForeignKey("employees.id"))
    client_id = Column(Integer, ForeignKey("clients.id"))

    __table_args__ = (
        CheckConstraint(
            status.in_(["signed", "pending", "cancelled"]), name="valid_status"
        ),
    )
