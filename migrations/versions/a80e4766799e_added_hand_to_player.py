"""added hand to Player

Revision ID: a80e4766799e
Revises: e288fb6230f2
Create Date: 2024-03-31 20:27:39.647506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a80e4766799e'
down_revision = 'e288fb6230f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hand',
    sa.Column('player_id', sa.Integer(), nullable=False),
    sa.Column('deck_card_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['deck_card_id'], ['deck_card.id'], ),
    sa.ForeignKeyConstraint(['player_id'], ['player.id'], ),
    sa.PrimaryKeyConstraint('player_id', 'deck_card_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hand')
    # ### end Alembic commands ###
