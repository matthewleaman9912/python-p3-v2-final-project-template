#lib/models/categories.py
from models.__init__ import CURSOR, CONN

class Categories:
    
    all = {}

    def __init__(self, category, id=None):
        self.id = id
        self.category = category

    def __repr__(self):
        return f"{self.category} Category Movies"
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category):
            self._category = category
        else:
            raise ValueError(
                "Please try again! Category must be a movie genre!"
            )
        
    @classmethod
    def create_table(cls):
        """ Create a table with id and category """
        sql = """
            CREATE TABLE IF NOT EXISTS categories(
            id INTEGER PRIMARY KEY,
            category TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop table that contains category instances """
        sql = """
            DROP TABLE IF EXISTS categories;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with name of the category
        Update with object id using the primary key for the new row
        Save the object in local dictionary using table """
        sql = """
            INSERT INTO categories (category)
            VALUES (?)    
        """
        CURSOR.execute(sql, (self.category,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, category1):
        """ Initialize a new category instance and save in the database """
        category_name = cls(category1)
        category_name.save()
        return category_name
    
    def update(self):
        """ update the table row with the category """
        sql = """
            UPDATE categories
            SET category = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.category, self.id))
        CONN.commit()

    def delete(self):
        """ Delete the row in the categories table and reassign the id attribute """
        sql = """
            DELETE FROM categories
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """ Return a category from the table """

        selection = cls.all.get(row[0])
        if selection:
            selection.category = row[1]
        else:
            selection = cls(row[1])
            selection.id = row[0]
            cls.all[selection.id] = selection
        return selection
    
    @classmethod
    def get_all(cls):
        """ Return a list of categories in a table """
        sql = """
            SELECT *
            FROM categories
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """ return a category mathcing the id """
        sql = """
            SELECT *
            FROM categories
            WHERE id = ?    
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_category(cls, category):
        """ return a category matching the category name """
        sql = """
            SELECT *
            FROM categories
            WHERE category is ?
        """
        row = CURSOR.execute(sql, (category,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    
            