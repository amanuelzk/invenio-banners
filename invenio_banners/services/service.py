# -*- coding: utf-8 -*-
#
# Copyright (C) 2022-2023 CERN.
#
# Invenio-Banners is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Banner Service API."""

import distutils.util

import arrow
from invenio_records_resources.services import RecordService
from invenio_records_resources.services.base import LinksTemplate
from invenio_records_resources.services.base.utils import map_search_params
from sqlalchemy import func

from ..records.models import BannerModel


class BannerService(RecordService):
    """Banner Service."""

    def read(self, identity, id):
        """Retrieve a banner."""
        self.require_permission(identity, "read")

        banner = self.record_cls.get(id)

        return self.result_item(
            self,
            identity,
            banner,
            links_tpl=self.links_item_tpl,
        )

    def search(self, identity, params):
        """Search for banners matching the querystring."""
        self.require_permission(identity, "search")

        search_params = map_search_params(self.config.search, params)

        query_param = search_params["q"]
        filters = []

        if query_param:
            filters.extend(
                [
                    BannerModel.repo_name.ilike(f"%{query_param}%"),
                    BannerModel.oai_url.ilike(f"%{query_param}%"),
                    BannerModel.set_name.ilike(f"%{query_param}%"),
                ]
            )
            bool_value = self._validate_bool(query_param)
            if bool_value is not None:
                filters.extend(
                    [
                        BannerModel.active.is_(bool_value),
                    ]
                )

            datetime_value = self._validate_datetime(query_param)
            if datetime_value is not None:
                filters.extend(
                    [
                        # func.date(BannerModel.start_datetime) == datetime_value,
                        # func.date(BannerModel.end_datetime) == datetime_value,
                        func.date(BannerModel.created) == datetime_value,
                        func.date(BannerModel.updated) == datetime_value,
                    ]
                )

        banners = self.record_cls.search(search_params, filters)

        return self.result_list(
            self,
            identity,
            banners,
            params=search_params,
            links_tpl=LinksTemplate(self.config.links_search, context={"args": params}),
            links_item_tpl=self.links_item_tpl,
        )

    def create(self, identity, data, raise_errors=True):
        """Create a banner."""
        self.require_permission(identity, "create")

        # validate data
        valid_data, errors = self.schema.load(
            data,
            context={"identity": identity},
            raise_errors=False,
        )

        # create the banner with the specified data
        banner = self.record_cls.create(valid_data)

        return self.result_item(
            self, identity, banner, links_tpl=self.links_item_tpl, errors=errors
        )

    def delete(self, identity, id):
        """Delete a banner from database."""
        self.require_permission(identity, "delete")

        banner = self.record_cls.get(id)

        self.record_cls.delete(banner)

        return self.result_item(self, identity, banner, links_tpl=self.links_item_tpl)

    def update(self, identity, id, data):
        """Update a banner."""
        self.require_permission(identity, "update")

        banner = self.record_cls.get(id)

        # validate data
        valid_data, errors = self.schema.load(
            data,
            context={"identity": identity},
            raise_errors=True,
        )

        self.record_cls.update(valid_data, id)

        return self.result_item(
            self,
            identity,
            banner,
            links_tpl=self.links_item_tpl,
        )

    def disable_expired(self, identity):
        """Disable expired banners."""
        self.require_permission(identity, "disable")
        self.record_cls.disable_expired()

    def _validate_bool(self, value):
        try:
            bool_value = distutils.util.strtobool(value)
        except ValueError:
            return None
        return bool(bool_value)

    def _validate_datetime(self, value):
        try:
            date_value = arrow.get(value).date()
        except ValueError:
            return None
        return date_value
