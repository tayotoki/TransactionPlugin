import json

import pytest

from utils.json_handler import JSONHandler


@pytest.fixture
def json_data(tmp_path):
    data = [
        {},
        {
            "id": 1,
            "inner": {
                "inner_1": {
                    "inner_2": {
                        "inner_3": {
                            "data": "some_data"
                        }
                    }
                }
            }
        }
    ]

    path = tmp_path / "test_data.json"

    with open(path, "w") as test_data:
        test_data.write(json.dumps(data))

    return path


class TestJSONHandler:
    def test_get_data(self, json_data):
        handler = JSONHandler(data_path=json_data)
        data = handler.get_data()

        assert list(data) == [
            {"id": 1, "data": "some_data"}
        ]
