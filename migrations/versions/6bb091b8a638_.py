"""empty message

Revision ID: 6bb091b8a638
Revises: ef53064aa167
Create Date: 2024-04-29 18:50:40.743099

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6bb091b8a638'
down_revision = 'ef53064aa167'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('trainer_data', schema=None) as batch_op:
        batch_op.add_column(sa.Column('trainer', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'trainer', ['trainer'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('trainer_data', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('trainer')

    # ### end Alembic commands ###