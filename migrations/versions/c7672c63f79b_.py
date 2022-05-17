"""empty message

Revision ID: c7672c63f79b
Revises: 9714be578d26
Create Date: 2022-05-13 21:28:21.076297

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7672c63f79b'
down_revision = '9714be578d26'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('deadline', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task', 'deadline')
    # ### end Alembic commands ###