from google.cloud import datastore
from dataclasses import asdict
from .models import Post


def create_post(client: datastore.Client, post: Post):
    key = client.key("Posts")
    ent = datastore.Entity(key=key)
    ent.update(asdict(post))
    return ent
