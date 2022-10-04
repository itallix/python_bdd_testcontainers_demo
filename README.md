# `bdd_testcontainers_demo`

![BDD Tests](https://github.com/itallix/py_bdd_testcontainers_demo/actions/workflows/test.yaml/badge.svg)

The purpose of this code is to demonstrate the technique of testing the data
migration scenario with [`pytest-bdd`](https://github.com/pytest-dev/pytest-bdd)
 and [`testcontainers`](https://github.com/testcontainers/testcontainers-python).
When the nature of the source and target data is quite different (e.g. SQL -> NoSQL),
and the mapping between those requires building additional logic. Then testing and
having fast development feedback loop becomes very important.

As a source for data migration here, we use MSSQL DB and as a target - Google Datastore.
However, this testing recipe could be easily adapted to many types of data sources/targets.

## Mapping from MSSSQL to Datastore

The following schema shows high level overview of the mapping that we are
going to use in our example:

![Mapping](./doc/sql_to_datastore_mapping.svg)

-   Source data lives in the SQL DB and is scattered in various tables
-   Target data should live in the NoSQL store and capture all source data in
the single kind
-   Mapping between these two assumes building some SQL query and transforming
some data

## Running tests

### Prerequisites

-   Make sure that you have [Poetry](https://python-poetry.org/docs/) installed 
for dependency management
-   Depending on your system, `pyodbc` might require additional binary dependency,
see more [here](https://pypi.org/project/pyodbc/)
-   Initialize an environment with `poetry install`

```bash
poetry run pytest tests/bdd
```
