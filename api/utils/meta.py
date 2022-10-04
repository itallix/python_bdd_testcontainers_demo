import json
from typing import Tuple, List


def convert_meta(meta: List[Tuple[str, str]]) -> str:
    return { m[0]:m[1] for m in meta }
