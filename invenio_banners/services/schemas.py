# -*- coding: utf-8 -*-
#
# Copyright (C) 2022-2023 CERN.
#
# Invenio-Banners is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Banners schema."""

from datetime import datetime, timezone

from invenio_records_resources.services.records.schema import BaseRecordSchema
from marshmallow import fields
from marshmallow_utils.fields import TZDateTime


class BannerSchema(BaseRecordSchema):
    """Schema for banners."""

    # message = fields.String(required=True)
    # url_path = fields.String(allow_none=True)
    # category = fields.String(required=True)
    # start_datetime = fields.DateTime(
    #     required=True,
    #     metadata={"default": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")},
    # )
    # end_datetime = fields.DateTime(allow_none=True)
    # active = fields.Boolean(required=True, metadata={"default": True})
    # created = TZDateTime(timezone=timezone.utc, format="iso", dump_only=True)
    # updated = TZDateTime(timezone=timezone.utc, format="iso", dump_only=True)

    message = fields.String(required=False)
    url_path = fields.String(allow_none=True)
    category = fields.String(required=False)
    start_datetime = fields.DateTime(
        required=False,
        metadata={"default": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")},
    )
    end_datetime = fields.DateTime(allow_none=True)
    active = fields.Boolean(required=False, metadata={"default": False})
    repo_name = fields.String(required=True)
    oai_url = fields.String(required=True)
    set_name = fields.String(required=False)
    meta_prefix = fields.String(required=False)
    created = TZDateTime(timezone=timezone.utc, format="iso", dump_only=True)
    updated = TZDateTime(timezone=timezone.utc, format="iso", dump_only=True)

