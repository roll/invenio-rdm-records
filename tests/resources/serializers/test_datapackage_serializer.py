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


def test_data_package_serializer_minimal_record(minimal_record_to_dict):
    serializer = DataPackageSerializer()
    serialized_record = serializer.dump_obj(minimal_record_to_dict)

    assert serialized_record == {
        "$schema": "https://datapackage.org/profiles/2.0/datapackage.json"
    }
