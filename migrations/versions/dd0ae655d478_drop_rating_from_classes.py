"""drop rating from classes

Revision ID: dd0ae655d478
Revises: c435fc4ba930
Create Date: 2025-07-22 16:32:05.997906

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'dd0ae655d478'
down_revision = 'c435fc4ba930'
branch_labels = None
depends_on = None



def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('classes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rating', sa.Float(), nullable=True))
        batch_op.drop_constraint(batch_op.f('classes_cancelled_by_fkey'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('classes_rescheduled_by_fkey'), type_='foreignkey')
        batch_op.drop_column('original_date')
        batch_op.drop_column('rescheduled_at')
        batch_op.drop_column('rescheduled_by')
        batch_op.drop_column('reschedule_reason')
        batch_op.drop_column('cancelled_by')
        batch_op.drop_column('template_name')
        batch_op.drop_column('original_time')
        batch_op.drop_column('cancellation_reason')
        batch_op.drop_column('cancelled_at')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('classes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cancelled_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('cancellation_reason', sa.TEXT(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('original_time', postgresql.TIME(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('template_name', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('cancelled_by', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('reschedule_reason', sa.TEXT(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('rescheduled_by', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('rescheduled_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('original_date', sa.DATE(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key(batch_op.f('classes_rescheduled_by_fkey'), 'users', ['rescheduled_by'], ['id'])
        batch_op.create_foreign_key(batch_op.f('classes_cancelled_by_fkey'), 'users', ['cancelled_by'], ['id'])
        batch_op.drop_column('rating')

    # ### end Alembic commands ###
