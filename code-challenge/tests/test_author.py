# tests/test_author.py
import pytest
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from lib.db.seed import seed_database

@pytest.fixture(autouse=True)
def setup_database():
    seed_database()

def test_author_creation():
    author = Author.find_by_name("John Doe")
    assert author is not None
    assert author.name == "John Doe"

def test_author_articles():
    author = Author.find_by_name("John Doe")
    articles = author.articles()
    assert len(articles) >= 2
    assert any(article.title == "Python Programming" for article in articles)

def test_author_magazines():
    author = Author.find_by_name("John Doe")
    magazines = author.magazines()
    assert len(magazines) >= 2
    assert any(magazine.name == "Tech Today" for magazine in magazines)