"""Added a tables

Revision ID: e6cd5035e231
Revises: 21b4ad6147fb
Create Date: 2017-10-31 15:07:09.736591

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6cd5035e231'
down_revision = '21b4ad6147fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('science', sa.String(length=255), nullable=True),
    sa.Column('tech', sa.String(length=255), nullable=True),
    sa.Column('innovation', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pitches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('review', sa.String(length=255), nullable=True),
    sa.Column('user_id_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.ForeignKeyConstraint(['user_id_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('results')
    op.drop_constraint('users_result_id_fkey', 'users', type_='foreignkey')
    op.drop_column('users', 'science')
    op.drop_column('users', 'technology')
    op.drop_column('users', 'result_id')
    op.drop_column('users', 'innovation')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('innovation', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('result_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('technology', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('science', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.create_foreign_key('users_result_id_fkey', 'users', 'results', ['result_id'], ['id'])
    op.create_table('results',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('review', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('voteup', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('votedown', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='results_pkey')
    )
    op.drop_table('pitches')
    op.drop_table('categories')
    # ### end Alembic commands ###
