"""empty message

Revision ID: d85fead83332
Revises: 
Create Date: 2023-02-24 20:50:03.043629

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd85fead83332'
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
    op.create_table('historia',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('edad', sa.Integer(), nullable=False),
    sa.Column('peso', sa.Integer(), nullable=False),
    sa.Column('telef', sa.Integer(), nullable=False),
    sa.Column('correo', sa.String(), nullable=True),
    sa.Column('direccion', sa.String(), nullable=True),
    sa.Column('paisRes', sa.String(), nullable=True),
    sa.Column('sexo', sa.String(), nullable=True),
    sa.Column('alt', sa.String(), nullable=True),
    sa.Column('cirugiasAnt', sa.String(), nullable=True),
    sa.Column('alergias', sa.String(), nullable=True),
    sa.Column('obs', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pago',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('id_passport', sa.String(length=20), nullable=False),
    sa.Column('payment_method', sa.String(length=20), nullable=False),
    sa.Column('confirmation_number', sa.Integer(), nullable=False),
    sa.Column('transaction_person', sa.String(length=20), nullable=False),
    sa.Column('image_of_payment', sa.String(length=200), nullable=False),
    sa.Column('image_id', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('confirmation_number')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pago')
    op.drop_table('historia')
    op.drop_table('user')
    # ### end Alembic commands ###
