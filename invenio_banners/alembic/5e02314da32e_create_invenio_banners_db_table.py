#
# This file is part of Invenio.
# Copyright (C) 2016-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Create invenio-banners db table."""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "5e02314da32e"
down_revision = "e40d93d99040"
branch_labels = ()
depends_on = None


def upgrade():
    """Upgrade database."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "banners",
        sa.Column("created", sa.DateTime(), nullable=False),
        sa.Column("updated", sa.DateTime(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("message", sa.Text(), nullable=True),
        sa.Column("url_path", sa.String(length=255), nullable=True),
        sa.Column("category", sa.String(length=20), nullable=True),
        sa.Column("start_datetime", sa.DateTime(), nullable=True),
        sa.Column("end_datetime", sa.DateTime(), nullable=True),
        sa.Column("active", sa.Boolean(name="active"), nullable=True),
        sa.Column("repo_name", sa.Text(), nullable=True),
        sa.Column("oai_url", sa.Text(), nullable=True),
        sa.Column("set_name", sa.Text(), nullable=True),
        sa.Column("meta_prefix", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_banners")),
    )
    # ### end Alembic commands ###


def downgrade():
    """Downgrade database."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("banners")
    # ### end Alembic commands ###
