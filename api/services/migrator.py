from typing import Any, Callable, List, Tuple, Union
import pyodbc
from sqlalchemy.engine import Connection
from api.da import db, ds
from google.cloud import datastore


def migrate_posts_by_ids(
    posts_ids: List[int], context: Tuple[Connection, datastore.Client] = None
) -> str:
    return _migrate_items_by_ids(posts_ids, db.load_posts, ds.write_posts, context)


def _migrate_items_by_ids(
    ids: List[int],
    loader_fn: Callable[[Connection, dict], List],
    writer_fn: Callable[[datastore.Client, List[Union[pyodbc.Row, Any]]], None],
    context: Tuple[Connection, datastore.Client],
) -> str:
    conn, client = context
    rows = loader_fn(conn, ids)
    writer_fn(client, rows)

    return f"Migrated {len(rows)}..."
