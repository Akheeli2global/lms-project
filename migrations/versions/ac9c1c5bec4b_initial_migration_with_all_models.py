"""Initial migration with all models

Revision ID: ac9c1c5bec4b
Revises: 
Create Date: 2025-07-12 12:49:31.056614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac9c1c5bec4b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tutors', schema=None) as batch_op:
        batch_op.add_column(sa.Column('test_score', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('test_date', sa.Date(), nullable=True))
        batch_op.add_column(sa.Column('test_notes', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tutors', schema=None) as batch_op:
        batch_op.drop_column('test_notes')
        batch_op.drop_column('test_date')
        batch_op.drop_column('test_score')

    # ### end Alembic commands ###
