"""empty message

Revision ID: 70cd08c55e6b
Revises: b8cfbc00158e
Create Date: 2023-03-04 12:02:21.716377

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70cd08c55e6b'
down_revision = 'b8cfbc00158e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('_password', sa.LargeBinary(), nullable=True))
        batch_op.drop_column('surname')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('surname', sa.VARCHAR(length=80), nullable=True))
        batch_op.drop_column('_password')

    # ### end Alembic commands ###
