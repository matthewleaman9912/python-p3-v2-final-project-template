import sqlite3

CONN = sqlite3.connect('movies.db')
CURSOR = CONN.cursor()
