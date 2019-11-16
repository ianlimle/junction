"""empty message

Revision ID: 254e609ac29c
Revises: b39606583c06
Create Date: 2019-11-16 15:39:11.012879

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '254e609ac29c'
down_revision = 'b39606583c06'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('skincare', sa.Column('product_id', sa.String(length=100), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('skincare', 'product_id')
    # ### end Alembic commands ###