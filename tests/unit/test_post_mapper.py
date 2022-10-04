from api.da.ds.row_mappers import post_mapper


def test_post_mapper():
    input = (1, "title", ["cat1", "cat2"], [("key1", "content1"), ("key2", "content2")])
    post = post_mapper(input)
    assert post.legacy_id == 1
    assert post.title == "title"
    assert post.categories == ["cat1", "cat2"]
    assert post.meta == { "key1": "content1", "key2": "content2" }
