"""Initial Migration

Revision ID: a0993d1f7d7a
Revises: 540ba63a84e2
Create Date: 2018-09-12 14:59:58.356037

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a0993d1f7d7a'
down_revision = '540ba63a84e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('opinion', sa.String(length=255), nullable=True),
    sa.Column('time_posted', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('pitches_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitches_id'], ['pitches.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('comment')
    op.add_column('categories', sa.Column('description', sa.String(length=255), nullable=True))
    op.add_column('categories', sa.Column('name', sa.String(length=255), nullable=True))
    op.drop_column('categories', 'category_description')
    op.drop_column('categories', 'name_category')
    op.add_column('pitches', sa.Column('category_id', sa.Integer(), nullable=True))
    op.add_column('pitches', sa.Column('content', sa.String(), nullable=True))
    op.create_foreign_key(None, 'pitches', 'categories', ['category_id'], ['id'])
    op.drop_column('pitches', 'pitch')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('pitch', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.drop_column('pitches', 'content')
    op.drop_column('pitches', 'category_id')
    op.add_column('categories', sa.Column('name_category', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('categories', sa.Column('category_description', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('categories', 'name')
    op.drop_column('categories', 'description')
    op.create_table('comment',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('pitch_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('comment', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], name='comment_pitch_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='comment_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='comment_pkey')
    )
    op.drop_table('comments')
    # ### end Alembic commands ###
