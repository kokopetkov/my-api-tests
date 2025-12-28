import json
from importlib import resources
import os
from pathlib import Path
from typing import List, Type, TypeVar
from pydantic import BaseModel

T = TypeVar('T', bound=BaseModel)

def get_data_path():
    # Взимаме пътя от конфигурацията, а не го "изчисляваме"
    relative_path = os.getenv("USERS_DATA_PATH")
    return Path(relative_path).absolute()


def read_json_resource(package: str, filename: str, model: Type[T]) -> List[T]:
    source = resources.files(package).joinpath(filename)

    with source.open("r", encoding="utf-8") as f:
        raw_data = json.load(f)
        return [model(**item) for item in raw_data]
