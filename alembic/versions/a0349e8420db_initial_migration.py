"""initial_migration

Revision ID: a0349e8420db
Revises: 
Create Date: 2024-03-25 23:23:58.675153

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a0349e8420db'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('phone_number', sa.String(length=15), nullable=True),
    sa.Column('company_name', sa.String(length=255), nullable=True),
    sa.Column('created_on', sa.Date(), nullable=True),
    sa.Column('updated_on', sa.Date(), nullable=True),
    sa.Column('sales_employee_id', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=255), nullable=True),
    sa.Column('department', sa.String(length=255), nullable=True),
    sa.CheckConstraint("department IN ('sales', 'support', 'management')", name='valid_department'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contracts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.Date(), nullable=True),
    sa.Column('status', sa.String(length=255), nullable=True),
    sa.Column('total_amount', sa.Float(), nullable=True),
    sa.Column('left_amount', sa.Float(), nullable=True),
    sa.Column('sales_employee_id', sa.String(length=255), nullable=True),
    sa.Column('management_employee_id', sa.String(length=255), nullable=True),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.CheckConstraint("status IN ('signed', 'pending', 'cancelled')", name='valid_status'),
    sa.ForeignKeyConstraint(['client_id'], ['clients.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.Column('location', sa.String(length=255), nullable=True),
    sa.Column('attendees', sa.Integer(), nullable=True),
    sa.Column('notes', sa.String(length=255), nullable=True),
    sa.Column('support_employee_id', sa.String(length=255), nullable=True),
    sa.Column('management_employee_id', sa.String(length=255), nullable=True),
    sa.Column('contrat_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['contrat_id'], ['contracts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('events')
    op.drop_table('contracts')
    op.drop_table('employees')
    op.drop_table('clients')
    # ### end Alembic commands ###