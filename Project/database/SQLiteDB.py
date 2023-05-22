import sqlite3
from classes.book import Book

conn = sqlite3.connect(':memory:')
c = conn.cursor()

c.execute("""CREATE TABLE books (

)""")