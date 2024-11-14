#lib/models/movies.py
from models.__init__ import CURSOR,CONN
from models.categories import Categories

class Movies:

    all = {}

    def __init__(self, title, length, actor, category_id, id=None):
        self.id = id
        self.title = title
        self.length = length
        self.actor = actor
        self.category_id = category_id

    def __repr__(self):
        return(
            f"<Movie {self.id}: {self.title}, {self.length}, {self.actor}, " +
            f"Category: {self.category_id}>"
        )
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title):
            self._title = title
        else:
            raise ValueError(
                "Please try again with your movie title!"
            )
    
    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, length):
        if type(length) is int:
            self._length = length
        else: 
            raise ValueError(
                "Please try again! Your movie length must be in minutes!"
            )
    
    @property
    def actor(self):
        return self._actor
    
    @actor.setter
    def actor(self, actor):
        if isinstance(actor, str) and len(actor):
            self._actor = actor
        else:
            raise ValueError(
                "Please try again! Your actor must have a name!"
            )
    
    @property
    def category_id(self):
        return self._category_id
    
    @category_id.setter
    def category_id(self, category_id):
        if type(category_id) is int and Categories.find_by_id(category_id):
            self._category_id = category_id
        else:
            raise ValueError(
                "Please try again! Select your category once again!"
            )
    
    @classmethod
    def create_table(cls):
        """ create a new table of the attributes of Movies """
        sql = """
            CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY,
            title TEXT,
            length INTEGER,
            actor TEXT,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop table with Movies """
        sql = """
            DROP TABLE IF EXISTS movies;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with movie attributes, with an updated object id and save the object in the local dictionary """
        sql = """
                INSERT INTO movies (title, length, actor, category_id)
                VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.title, self.length, self.actor, self.category_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row relating to current Movie """
        sql = """
            UPDATE movies
            SET title = ?, length = ?, actor = ?, category_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.title, self.length, self.actor, self.category_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row of selected movie and reassign the current id"""

        sql = """
            DELETE FROM movies
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, title, length, actor, category_id):
        """ Create a new movie and save as a new object """
        movie = cls(title, length, actor, category_id)
        movie.save()
        return movie
    
    @classmethod
    def instance_from_db(cls, row):
        """ Return movie and its attributes """

        movie = cls.all.get(row[0])
        if movie:
            movie.title = row[1]
            movie.length = row[2]
            movie.actor = row[3]
            movie.category_id = row[4]
        else:
            movie = cls(row[1], row[2], row[3], row[4])
            movie.id = row[0]
            cls.all[movie.id] = movie
        return movie
    
    @classmethod
    def get_all(cls):
        """ Return a list returning one row """
        sql = """
            SELECT *
            FROM movies
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """ Return movie and row based on id """
        sql = """
            SELECT *
            FROM movies
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_category(cls, category_id):
        """ Return movie with matching category """
        sql = """
            SELECT *
            FROM movies
            WHERE category_id is ?
        """

        rows = CURSOR.execute(sql, (category_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_title(cls, title):
        """ Return movie with mathcing title """
        sql = """
            SELECT *
            FROM movies
            WHERE title is ?
        """

        row = CURSOR.execute(sql, (title,)).fetchone()
        return cls.instance_from_db(row) if row else None
    