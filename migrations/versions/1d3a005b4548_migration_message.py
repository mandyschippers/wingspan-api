"""migration message

Revision ID: 1d3a005b4548
Revises: f979a7ff4129
Create Date: 2024-05-06 16:12:02.857790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d3a005b4548'
down_revision = 'f979a7ff4129'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('model_setting',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model_name', sa.String(length=256), nullable=True),
    sa.Column('model_description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('module_setting',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('module_name', sa.String(length=256), nullable=True),
    sa.Column('module_description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('segment_settings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('segment_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('model_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('module_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'model_setting', ['model_id'], ['id'])
        batch_op.create_foreign_key(None, 'conversation_segment', ['segment_id'], ['id'])
        batch_op.create_foreign_key(None, 'module_setting', ['module_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('segment_settings', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('module_id')
        batch_op.drop_column('model_id')
        batch_op.drop_column('segment_id')

    op.drop_table('module_setting')
    op.drop_table('model_setting')
    # ### end Alembic commands ###
