from dataclasses import dataclass
from typing import List


@dataclass
class Post:
    title: str
    legacy_id: int
    categories: List[str]
    meta: dict[str, str]
