"""updating_contract_status

Revision ID: 8c8b25d44f32
Revises: b4b4afa14069
Create Date: 2024-05-01 21:59:31.344219

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "8c8b25d44f32"
down_revision: Union[str, None] = "b4b4afa14069"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.drop_constraint("valid_status", "contracts", type_="check")
    op.create_check_constraint(
        "valid_status",
        "contracts",
        sa.text("status IN ('validé', 'en attente', 'annulé')"),
    )


def downgrade():
    op.drop_constraint("valid_status", "contracts", type_="check")
