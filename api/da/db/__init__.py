from multiprocessing.sharedctypes import Value
from typing import List, Tuple
from sqlalchemy.engine import Connection
from . import query_posts


def load_posts(conn: Connection, post_ids: List[int]) -> List[Tuple]:
    return [
        tuple([*post, load_categories(conn, post[0]), load_meta(conn, post[0])])
        for post in conn.execute(query_posts.select_posts(post_ids)).all()
    ]


def load_categories(conn: Connection, post_id: int):
    cats = conn.execute(query_posts.select_categories(post_id)).all()
    return [c[0] for c in cats]


def load_meta(conn: Connection, post_id: int):
    meta = conn.execute(query_posts.select_meta(post_id)).all()
    return [(m[0], m[1]) for m in meta]
