"""relationships in segment settings module not model

Revision ID: 423ad603faac
Revises: 52131051ac40
Create Date: 2024-05-06 16:43:45.201320

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '423ad603faac'
down_revision = '52131051ac40'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('module_settings_join',
    sa.Column('module_id', sa.Integer(), nullable=False),
    sa.Column('settings_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['module_id'], ['module_setting.id'], ),
    sa.ForeignKeyConstraint(['settings_id'], ['segment_settings.id'], ),
    sa.PrimaryKeyConstraint('module_id', 'settings_id')
    )
    op.drop_table('model_settings_join')
    with op.batch_alter_table('segment_settings', schema=None) as batch_op:
        batch_op.drop_constraint('segment_settings_module_id_fkey', type_='foreignkey')
        batch_op.drop_column('module_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('segment_settings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('module_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('segment_settings_module_id_fkey', 'module_setting', ['module_id'], ['id'])

    op.create_table('model_settings_join',
    sa.Column('model_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('settings_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['model_id'], ['model_setting.id'], name='model_settings_join_model_id_fkey'),
    sa.ForeignKeyConstraint(['settings_id'], ['segment_settings.id'], name='model_settings_join_settings_id_fkey'),
    sa.PrimaryKeyConstraint('model_id', 'settings_id', name='model_settings_join_pkey')
    )
    op.drop_table('module_settings_join')
    # ### end Alembic commands ###
