from typing import List, Any, Tuple
from .crud import create_post
from .row_mappers import post_mapper
from google.cloud import datastore


def write_posts(client: datastore.Client, post_rows: List[Tuple[Any]]) -> None:
    batch = [create_post(client, post_mapper(row)) for row in post_rows]
    client.put_multi([b for b in batch if b])
