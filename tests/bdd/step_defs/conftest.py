import json
from typing import Any

from api.da import db
from pytest import fixture
from pytest_bdd import given, parsers
from sqlalchemy import create_engine
from sqlalchemy.engine import Connection
from testcontainers.mssql import SqlServerContainer
from tests.datastore import DatastoreContainer

from . import table_refs


@fixture(scope="session", autouse=True)
def mssql_connection() -> Connection:
    with SqlServerContainer(
        "mcr.microsoft.com/mssql/server:2017-latest"
    ) as mssql:
        engine = create_engine(mssql.get_connection_url())
        db.schema.metadata.create_all(engine)
        yield engine.connect()


@fixture(scope="session", autouse=True)
def gds_client():
    with DatastoreContainer() as ds:
        yield ds.get_client()


@fixture
def context() -> Any:
    class Context(object):
        pass

    return Context()


@given(parsers.parse("table {table_name} has {payload}"))
def table_insert(
    mssql_connection: Connection, context: Any, table_name: str, payload: str
) -> None:
    obj = json.loads(payload)
    mssql_connection.execute(table_refs[table_name].insert().values(obj))
    if not hasattr(context, "table_tracking"):
        context.table_tracking = []
    if table_name not in context.table_tracking:
        context.table_tracking.append(table_name)
