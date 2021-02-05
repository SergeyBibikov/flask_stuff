"""empty message

Revision ID: 04fd7d87d175
Revises: 
Create Date: 2021-02-05 20:11:36.336036

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04fd7d87d175'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('manufacturers', sa.Column('legal_form_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'manufacturers', 'legalforms', ['legal_form_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'manufacturers', type_='foreignkey')
    op.drop_column('manufacturers', 'legal_form_id')
    # ### end Alembic commands ###
