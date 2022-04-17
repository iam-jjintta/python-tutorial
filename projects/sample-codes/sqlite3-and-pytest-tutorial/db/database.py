
import sqlite3


class Test:
    __test__ = False


    def __init__(self, data1=None, data2=None):
        self.data1 = data1
        self.data2 = data2


class Query:
    create = '''
        CREATE TABLE my_test (
            no    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            data1 TEXT        NULL,
            data2 TEXT        NULL
        );
    '''
    select_all = 'SELECT * FROM my_test;'
    select_one = 'SELECT * FROM my_test WHERE no = ?;'
    insert = '''
        INSERT INTO my_test (data1, data2)
        VALUES (?, ?);
    '''
    update = '''
        UPDATE my_test
        SET
            data1 = ?,
            data2 = ?
        WHERE no = ?
    '''
    delete = 'DELETE FROM my_test WHERE no = ?'


class Database:

    def __init__(self):
        self.conn = sqlite3.connect('test.db')
        self.query = Query


    def create(self):
        result = self.execute(self.query.create)
        return result


    def get(self, where):
        result = self.fetch(
            self.query.select_one,
            where
        )[0]
        return result


    def get_all(self):
        result = self.fetch(self.query.select_all)
        return result


    def add(self, test):
        result = self.execute(
            self.query.insert,
            test.data1, test.data2
        )
        return result


    def edit(self, where, test):
        result = self.execute(
            self.query.update,
            test.data1, test.data2,
            where
        )
        return result


    def remove(self, where):
        result = self.execute(
            self.query.delete,
            where
        )
        return result


    def execute(self, query, *params):
        cur = self.conn.cursor()
        result = cur.execute(query, params)
        self.conn.commit()
        cur.close()
        return result


    def fetch(self, query, *params):
        cur = self.conn.cursor()
        cur.execute(query, params)
        result = cur.fetchall()
        cur.close()
        return tuple(result)
