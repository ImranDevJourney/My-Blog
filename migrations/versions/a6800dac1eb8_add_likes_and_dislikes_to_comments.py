"""Add likes and dislikes to comments

Revision ID: a6800dac1eb8
Revises: 
Create Date: 2024-10-07 04:06:56.556362

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6800dac1eb8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('likes', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('dislikes', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.drop_column('dislikes')
        batch_op.drop_column('likes')

    # ### end Alembic commands ###
