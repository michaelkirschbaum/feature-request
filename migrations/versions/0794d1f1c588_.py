"""empty message

Revision ID: 0794d1f1c588
Revises: None
Create Date: 2016-08-28 20:10:23.707803

"""

# revision identifiers, used by Alembic.
revision = '0794d1f1c588'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('request',
    sa.Column('title', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('title')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('request')
    ### end Alembic commands ###
