"""Initial migration

Revision ID: 84754bd13ab1
Revises: 
Create Date: 2023-11-03 12:52:50.413151

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84754bd13ab1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('servers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('guild', sa.BigInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('guild')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('discord_id', sa.BigInteger(), nullable=False),
    sa.Column('replace', sa.Boolean(), nullable=False),
    sa.Column('banned', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('discord_id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('admins_servers_association_table',
    sa.Column('server_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['server_id'], ['servers.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('server_id', 'user_id')
    )
    op.create_table('emotes',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('path', sa.String(length=128), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('path')
    )
    op.create_table('users_servers_association_table',
    sa.Column('server_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['server_id'], ['servers.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('server_id', 'user_id')
    )
    op.create_table('emotes_servers_association_table',
    sa.Column('server_id', sa.Integer(), nullable=False),
    sa.Column('emote_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['emote_id'], ['emotes.id'], ),
    sa.ForeignKeyConstraint(['server_id'], ['servers.id'], ),
    sa.PrimaryKeyConstraint('server_id', 'emote_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('emotes_servers_association_table')
    op.drop_table('users_servers_association_table')
    op.drop_table('emotes')
    op.drop_table('admins_servers_association_table')
    op.drop_table('users')
    op.drop_table('servers')
    # ### end Alembic commands ###