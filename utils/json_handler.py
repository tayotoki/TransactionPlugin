import json
from pathlib import Path
from typing import Generator

from ..settings import JSON_OPS_DATA


class JSONHandler:
    def __init__(self, data_path: Path = None):
        self.data: Path = data_path if data_path else JSON_OPS_DATA

    def get_data(self) -> Generator[dict, None, None]:
        with open(self.data) as file:
            for operation in iter(json.load(file)):
                yield self.parse_dict(operation)

    @staticmethod
    def parse_dict(data: dict):
        result_data = {}

        for key, value in data:
            if type(value) is dict:
                JSONHandler.parse_dict(value)

            result_data.update({key: value})

        return result_data
