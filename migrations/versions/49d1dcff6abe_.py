"""empty message

Revision ID: 49d1dcff6abe
Revises: 
Create Date: 2023-01-04 03:30:37.322207

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49d1dcff6abe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('films',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('director', sa.String(length=50), nullable=False),
    sa.Column('producer', sa.String(length=50), nullable=False),
    sa.Column('release_date', sa.String(length=50), nullable=False),
    sa.Column('episode_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('gender', sa.String(length=50), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.Column('skin_color', sa.String(length=50), nullable=False),
    sa.Column('eyes_color', sa.String(length=50), nullable=False),
    sa.Column('birth_year', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('diameter', sa.Integer(), nullable=False),
    sa.Column('gravity', sa.String(length=50), nullable=False),
    sa.Column('population', sa.Integer(), nullable=False),
    sa.Column('terrain', sa.String(length=50), nullable=False),
    sa.Column('climate', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('species',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('classification', sa.String(length=50), nullable=False),
    sa.Column('designation', sa.String(length=100), nullable=False),
    sa.Column('languaje', sa.String(length=100), nullable=False),
    sa.Column('skin_color', sa.String(length=100), nullable=False),
    sa.Column('eye_color', sa.String(length=50), nullable=False),
    sa.Column('average_lifespan', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('starships',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=False),
    sa.Column('manufacturer', sa.String(length=100), nullable=False),
    sa.Column('lenght', sa.Integer(), nullable=False),
    sa.Column('cargo_capacity', sa.Integer(), nullable=False),
    sa.Column('consumables', sa.Integer(), nullable=False),
    sa.Column('max_atmosphering_speed', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('token_blocklist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('jti', sa.String(length=36), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('token_blocklist', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_token_blocklist_jti'), ['jti'], unique=False)

    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=300), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=False),
    sa.Column('manufacturer', sa.String(length=100), nullable=False),
    sa.Column('lenght', sa.Integer(), nullable=False),
    sa.Column('cargo_capacity', sa.Integer(), nullable=False),
    sa.Column('consumables', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('favorite_type', sa.String(length=50), nullable=False),
    sa.Column('element_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorites')
    op.drop_table('vehicles')
    op.drop_table('user')
    with op.batch_alter_table('token_blocklist', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_token_blocklist_jti'))

    op.drop_table('token_blocklist')
    op.drop_table('starships')
    op.drop_table('species')
    op.drop_table('planets')
    op.drop_table('people')
    op.drop_table('films')
    # ### end Alembic commands ###
