from typing import List

from sqlalchemy import select
from sqlalchemy.sql.expression import Select

from .schema import post, post_category, category, post_meta


def select_posts(ids: List = None) -> Select:
    q = select(
        post.c.id,
        post.c.title
    )
    if ids:
        q = q.where(post.c.id.in_(ids))
    return q


def select_categories(post_id: int) -> Select:
    return select(category.c.title).join(post_category).where(
        post_category.c.postId == post_id
    )


def select_meta(post_id: int) -> Select:
    return select(post_meta.c.key, post_meta.c.content).join(post).where(
        post.c.id == post_id
    )
