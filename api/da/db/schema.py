from sqlalchemy import (
    Column,
    ForeignKey,
    Identity,
    Integer,
    MetaData,
    String,
    Table,
    text,
)

metadata = MetaData()

post = Table(
    "post",
    metadata,
    Column(
        "id", Integer, primary_key=True, nullable=False,
        server_default=Identity(start=1, increment=1),
    ),
    Column("title", String(50), nullable=False),
    Column("summary", String(100)),
)

post_category = Table(
    "post_category",
    metadata,
    Column(
        "postId",
        Integer,
        ForeignKey("post.id"),
        primary_key=True,
        nullable=False,
        server_default=text("0"),
    ),
    Column(
        "categoryId", 
        Integer,
        ForeignKey("category.id"),
        primary_key=True,
        nullable=False,
        server_default=text("0")
    )
)

category = Table(
    "category",
    metadata,
    Column(
        "id", Integer, primary_key=True, nullable=False,
        server_default=Identity(start=1, increment=1)
    ),
    Column("title", String(50), nullable=False),
)

post_meta = Table(
    "post_meta",
    metadata,
    Column(
        "id", Integer, primary_key=True, nullable=False,
        server_default=Identity(start=1, increment=1)
    ),
    Column("postId", Integer, ForeignKey("post.id"), nullable=False),
    Column("key", String(50), nullable=False),
    Column("content", String(100), nullable=False),
)
