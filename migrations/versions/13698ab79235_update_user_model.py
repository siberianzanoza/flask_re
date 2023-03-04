"""update user model

Revision ID: 13698ab79235
Revises: 70cd08c55e6b
Create Date: 2023-03-04 12:08:04.637608

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13698ab79235'
down_revision = '70cd08c55e6b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('fullname', sa.String(length=80), server_default='', nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('fullname')

    # ### end Alembic commands ###
