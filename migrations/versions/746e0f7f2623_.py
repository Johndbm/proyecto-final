"""empty message

Revision ID: 746e0f7f2623
Revises: 
Create Date: 2023-02-15 15:28:07.516579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '746e0f7f2623'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('lastname', sa.String(length=20), nullable=False),
    sa.Column('country', sa.String(length=30), nullable=False),
    sa.Column('city', sa.String(length=20), nullable=False),
    sa.Column('state', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('pago',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('id_passport', sa.String(length=20), nullable=False),
    sa.Column('payment_method', sa.String(length=20), nullable=False),
    sa.Column('confirmation_number', sa.Integer(), nullable=False),
    sa.Column('transaction_person', sa.String(length=20), nullable=False),
    sa.Column('proof_of_payment', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('confirmation_number'),
    sa.UniqueConstraint('id_passport')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pago')
    op.drop_table('user')
    # ### end Alembic commands ###