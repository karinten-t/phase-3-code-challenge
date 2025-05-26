
import pytest
from lib.models.article import Article
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.db.seed import seed_database

@pytest.fixture(autouse=True)
def setup_database():
    seed_database()

def test_article_creation():
    article = Article.find_by_id(1)
    assert article is not None
    assert article.title == "Python Programming"

def test_article_relationships():
    article = Article.find_by_id(1)
    author = article.author()
    magazine = article.magazine()
    assert author.name == "John Doe"
    assert magazine.name == "Tech Today"

def test_article_all():
    articles = Article.all()
    assert len(articles) >= 5