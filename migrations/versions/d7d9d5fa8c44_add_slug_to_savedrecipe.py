"""Add slug to SavedRecipe

Revision ID: d7d9d5fa8c44
Revises: 68fb96bf1f91
Create Date: 2025-04-19 17:13:58.561751

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7d9d5fa8c44'
down_revision = '68fb96bf1f91'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('recipe')
    op.drop_table('contact_message')
    op.drop_table('saved_recipe')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('saved_recipe',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('recipe_slug', sa.VARCHAR(length=100), nullable=False),
    sa.Column('category', sa.VARCHAR(length=50), nullable=False),
    sa.Column('saved_on', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contact_message',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), nullable=False),
    sa.Column('message', sa.TEXT(), nullable=False),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recipe',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), nullable=False),
    sa.Column('category', sa.VARCHAR(length=20), nullable=False),
    sa.Column('ingredients', sa.TEXT(), nullable=False),
    sa.Column('instructions', sa.TEXT(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=100), nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), nullable=False),
    sa.Column('password', sa.VARCHAR(length=200), nullable=False),
    sa.Column('reset_token', sa.VARCHAR(length=100), nullable=True),
    sa.Column('token_expiry', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###
