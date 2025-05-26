
import pytest
from lib.models.magazine import Magazine
from lib.models.author import Author
from lib.db.seed import seed_database

@pytest.fixture(autouse=True)
def setup_database():
    seed_database()

def test_magazine_creation():
    magazine = Magazine.find_by_name("Tech Today")
    assert magazine is not None
    assert magazine.name == "Tech Today"
    assert magazine.category == "Technology"

def test_magazine_articles():
    magazine = Magazine.find_by_name("Tech Today")
    articles = magazine.articles()
    assert len(articles) >= 2
    assert any(article.title == "Python Programming" for article in articles)

def test_magazine_contributors():
    magazine = Magazine.find_by_name("Tech Today")
    contributors = magazine.contributors()
    assert len(contributors) >= 1
    assert any(author.name == "John Doe" for author in contributors)

def test_top_publisher():
    top_pub = Magazine.top_publisher()
    assert top_pub is not None
    assert top_pub.name in ["Tech Today", "Science Weekly", "Business Insights"]