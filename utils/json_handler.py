import json
from pathlib import Path
from typing import Generator, Optional

from settings import JSON_OPS_DATA


class JSONHandler:
    def __init__(self, data_path: Path = None):
        self.data: Path = data_path if data_path else JSON_OPS_DATA

    def get_data(self) -> Generator[dict, None, None]:
        with open(self.data) as file:
            for operation in iter(json.load(file)):
                if operation:
                    yield self.parse_dict(operation)

    @staticmethod
    def parse_dict(data: dict, result_data: Optional[dict] = None):
        result_data = {} if not result_data else result_data

        for key, value in data.items():
            if type(value) is dict:
                JSONHandler.parse_dict(data[key], result_data)
            else:
                result_data.update({key: value})

        return result_data
