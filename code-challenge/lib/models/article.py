# lib/models/article.py
from lib.db.connection import get_connection

class Article:
    def __init__(self, title, author_id, magazine_id, id=None):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id:
            cursor.execute("""
                UPDATE articles 
                SET title = ?, author_id = ?, magazine_id = ? 
                WHERE id = ?
            """, (self.title, self.author_id, self.magazine_id, self.id))
        else:
            cursor.execute("""
                INSERT INTO articles (title, author_id, magazine_id) 
                VALUES (?, ?, ?)
            """, (self.title, self.author_id, self.magazine_id))
            self.id = cursor.lastrowid
        conn.commit()
        conn.close()
        return self

    def delete(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM articles WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()

    @classmethod
    def create(cls, title, author_id, magazine_id):
        article = cls(title, author_id, magazine_id)
        return article.save()

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(row['title'], row['author_id'], row['magazine_id'], row['id'])
        return None

    def author(self):
        from lib.models.author import Author
        return Author.find_by_id(self.author_id)

    def magazine(self):
        from lib.models.magazine import Magazine
        return Magazine.find_by_id(self.magazine_id)

    @classmethod
    def all(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles")
        rows = cursor.fetchall()
        conn.close()
        return [cls(row['title'], row['author_id'], row['magazine_id'], row['id']) for row in rows]