"""empty message

Revision ID: 15a8c12a44b7
Revises: 
Create Date: 2019-07-10 12:17:53.049781

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15a8c12a44b7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('currency',
    sa.Column('currency_id', sa.Integer(), nullable=False),
    sa.Column('iso_code', sa.String(length=3), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('symbol', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('currency_id'),
    sa.UniqueConstraint('iso_code')
    )
    op.create_table('currency_rate',
    sa.Column('currency_rate_id', sa.Integer(), nullable=False),
    sa.Column('iso_code', sa.String(length=3), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('rate', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('currency_rate_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('currency_rate')
    op.drop_table('currency')
    # ### end Alembic commands ###
