# lib/db/seed.py
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def seed_database():
    # Clear existing data
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM authors")
    cursor.execute("DELETE FROM magazines")
    conn.commit()
    conn.close()

    # Create authors
    author1 = Author.create("John Doe")
    author2 = Author.create("Jane Smith")
    author3 = Author.create("Bob Johnson")

    # Create magazines
    magazine1 = Magazine.create("Tech Today", "Technology")
    magazine2 = Magazine.create("Science Weekly", "Science")
    magazine3 = Magazine.create("Business Insights", "Business")

    # Create articles
    Article.create("Python Programming", author1.id, magazine1.id)
    Article.create("AI Revolution", author1.id, magazine1.id)
    Article.create("Quantum Computing", author2.id, magazine2.id)
    Article.create("Neural Networks", author1.id, magazine2.id)
    Article.create("Market Trends", author3.id, magazine3.id)
    Article.create("Startup Funding", author3.id, magazine3.id)
    Article.create("Blockchain Technology", author3.id, magazine1.id)

if __name__ == '__main__':
    from lib.db.connection import get_connection
    seed_database()
    print("Database seeded successfully!")