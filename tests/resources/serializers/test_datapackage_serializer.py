# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 Open Knowledge Foundation
#
# Invenio-RDM-Records is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Resources serializers tests."""

import pytest

from invenio_rdm_records.resources.serializers.datapackage import DataPackageSerializer
from invenio_rdm_records.resources.serializers.errors import VocabularyItemNotFoundError


def test_data_package_serializer_minimal_record(full_record_to_dict):
    serializer = DataPackageSerializer()
    serialized_record = serializer.dump_obj(full_record_to_dict)
    assert serialized_record == {
        "$schema": "https://datapackage.org/profiles/2.0/datapackage.json",
        "id": "https://handle.stage.datacite.org/10.1234/inveniordm.1234",
        "title": "InvenioRDM",
        "description": "<h1>A description</h1> <p>with HTML tags</p>",
        "version": "v1.0",
        "created": "2023-11-14T18:30:55.738898+00:00",
        "homepage": "https://127.0.0.1:5000/records/12345-abcde",
        "keywords": ["Abdominal Injuries", "custom"],
    }