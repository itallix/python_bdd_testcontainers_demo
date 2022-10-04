from os import getenv
from typing import Any

import requests
from sqlalchemy.engine import Connection

from api.da.db import schema

table_refs = schema.metadata.tables


def cleanup_sql(conn: Connection, context: Any) -> None:
    if hasattr(context, "table_tracking"):
        for t in reversed(context.table_tracking):
            conn.execute(table_refs[t].delete())
        context.table_tracking.clear()


def cleanup_datastore() -> None:
    resp = requests.post(f"{getenv('DATASTORE_HOST')}/reset")
    if resp.status_code != 200:
        raise ValueError(
            f"Some issue with cleaning Datastore, "
            f"status_code: {resp.status_code}"
        )
