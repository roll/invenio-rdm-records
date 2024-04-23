# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 Open Knowledge Foundation
#
# Invenio-RDM-Records is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Data Package based Schema for Invenio RDM Records."""

from marshmallow import Schema, fields


class DataPackageSchema(Schema):
    """Schema for Data Package in JSON."""

    profile = fields.Constant(
        "https://datapackage.org/profiles/2.0/datapackage.json", data_key="$schema"
    )
