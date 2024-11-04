from pathlib import Path

file_path = Path("test.txt").resolve()


# class MyCostomFileReaderContextManager:
#     def __init__(self, file_path):
#         self.file_path = file_path
#         self.file = None
#         self.closed = False

#     def __enter__(self):
#         self.file = open(self.file_path, "a+")
#         return self.file

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#         self.closed = True


# with MyCostomFileReaderContextManager(file_path) as file:
#     # write some text to the file
#     file.write("Hello, World")
#     print(file.read())
#     print(file.closed)  # False

# print(file.closed)  # True
# print(file.read())  # ValueError: I/O operation on closed file.

############################################# Function based context manager #############################################
from contextlib import contextmanager


@contextmanager
def my_context_manager(file_path):
    file = open(file_path, "a+")
    try:
        yield file  # generator
    finally:
        file.close()


with my_context_manager(file_path) as file:
    # write some text to the file
    file.write("Hello, World")
    print(file.read())
    print(file.closed)  # False

print(file.closed)  # True

############################################# DataBases context manager #############################################
import sqlite3


class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()


with Database("test.db") as cursor:
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS test_table (id INTEGER PRIMARY KEY, name TEXT)"
    )
    cursor.execute("INSERT INTO test_table (name) VALUES ('John')")
    cursor.execute("SELECT * FROM test_table")
    data = cursor.fetchall()

print(data)
