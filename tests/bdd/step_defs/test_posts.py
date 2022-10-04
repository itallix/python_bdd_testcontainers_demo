import json
from typing import Any

from pytest_bdd import parsers, scenarios, then, when
from sqlalchemy.engine import Connection
from google.cloud import datastore

from api.services import migrator

from . import cleanup_datastore, cleanup_sql

scenarios("../features/posts.feature")


@when(
    parsers.parse(
        "the post migration is triggered for postId={post_id:d}"
    )
)
def trigger_migration_for(
    mssql_connection: Connection, gds_client: datastore.Client, post_id: int
) -> None:
    migrator.migrate_posts_by_ids(
        [post_id], (mssql_connection, gds_client)
    )


@then(parsers.parse("post migrated as {payload}"))
def check_post_as(gds_client: datastore.Client, payload: str) -> None:
    expected = json.loads(payload)
    q = gds_client.query(
        kind="Posts",
        filters=[("legacy_id", "=", expected["legacy_id"])],
    )
    post = list(q.fetch())[0]
    embedded = { 
        p[0]: dict(p[1].items()) for p in post.items() 
        if isinstance(p[1], datastore.Entity) 
    }
    actual = dict(post.items()) | embedded
    assert actual == expected


@then(parsers.parse("{count:d} posts migrated"))
@then(parsers.parse("{count:d} post migrated"))
def check_posts(
    mssql_connection: Connection,
    gds_client: datastore.Client,
    context: Any,
    count: int,
) -> None:
    query = gds_client.query(kind="Posts")
    res = list(query.fetch())
    assert len(res) == count
    cleanup_sql(mssql_connection, context)
    cleanup_datastore()
