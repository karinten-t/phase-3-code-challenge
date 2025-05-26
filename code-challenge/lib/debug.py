# lib/debug.py
from lib.db.connection import get_connection
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from lib.db.seed import seed_database

def debug():
    # Seed the database
    seed_database()
    
    # Example queries
    print("All authors:")
    authors = [Author.find_by_id(i) for i in range(1, 4)]
    for author in authors:
        print(f"{author.id}: {author.name}")
    
    print("\nAll magazines:")
    magazines = [Magazine.find_by_id(i) for i in range(1, 4)]
    for magazine in magazines:
        print(f"{magazine.id}: {magazine.name} ({magazine.category})")
    
    print("\nAll articles:")
    articles = Article.all()
    for article in articles:
        print(f"{article.id}: {article.title} by {article.author().name} in {article.magazine().name}")
    
    print("\nTesting relationships:")
    john = Author.find_by_name("John Doe")
    print(f"\nArticles by {john.name}:")
    for article in john.articles():
        print(f"- {article.title}")
    
    print(f"\nMagazines {john.name} has contributed to:")
    for magazine in john.magazines():
        print(f"- {magazine.name} ({magazine.category})")
    
    tech_today = Magazine.find_by_name("Tech Today")
    print(f"\nAuthors who have written for {tech_today.name}:")
    for author in tech_today.contributors():
        print(f"- {author.name}")
    
    print("\nTop publisher:")
    top_pub = Magazine.top_publisher()
    print(f"{top_pub.name} with {len(top_pub.articles())} articles")

if __name__ == '__main__':
    debug()