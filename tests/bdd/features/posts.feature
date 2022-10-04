Feature: Posts migration path

  Scenario: Test that a selected post can be migrated with categories
    Given Table post has { "id": 45, "title": "Welcome to BDD" }
    And Table category has { "id": 1, "title": "python" }
    And Table category has { "id": 2, "title": "pytest-bdd" }
    And Table post_category has { "postId": 45, "categoryId": 1 }
    And Table post_category has { "postId": 45, "categoryId": 2 }
    When the post migration is triggered for postId=45
    Then post migrated as { "title": "Welcome to BDD", "legacy_id": 45, "categories": ["python", "pytest-bdd"], "meta": {} }
    And 1 post migrated

  Scenario: Test that a selected post can be migrated with meta
    Given Table post has { "id": 47, "title": "Welcome to testcontainers" }
    And Table post_meta has { "postId": 47, "key": "author", "content": "Vitalii Karniushin" }
    And Table post_meta has { "postId": 47, "key": "company", "content": "CTS" }
    When the post migration is triggered for postId=47
    Then post migrated as { "title": "Welcome to testcontainers", "legacy_id": 47, "categories": [], "meta": { "author": "Vitalii Karniushin", "company": "CTS" } }
    And 1 post migrated
