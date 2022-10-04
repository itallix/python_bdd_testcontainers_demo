from typing import Any, Tuple

from .models import Post


def post_mapper(row: Tuple[Any]) -> Post:
    return Post(
        title=row[1],
        legacy_id=row[0],
        categories=row[2],
        meta={ m[0]: m[1] for m in row[3] }
    )
