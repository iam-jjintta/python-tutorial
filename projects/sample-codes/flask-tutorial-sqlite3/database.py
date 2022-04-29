'''
흔한 찐따의 SQLite3 튜토리얼 - 주소록 만들기
SQLite3 Tutorial (AddressBook): https://github.com/iam-jjintta/python-tutorial/blob/main/projects/sample-codes/12.%20address_book_using_sqlite3.py
'''

import sqlite3


class Address:
    '''
    no: 고유 번호
    first_name: 성
    last_name: 이름
    email: 이메일
    phone_no: 휴대폰 번호
    home_address: 집 주소
    company: 학교/직장
    description: 설명
    '''

    def __init__(
        self,
        no,
        first_name, last_name,
        email=None, phone_no=None,
        home_address=None, company=None,
        description=None
    ):
        self.no = no
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_no = phone_no
        self.home_address = home_address
        self.company = company
        self.description = description


class AddressBook:

    def __init__(self, check_same_thread=False):
        self.db_name = 'address_book.db'
        self.conn = sqlite3.connect(
            self.db_name,
            # Flask-App Thread & Database Thread
            check_same_thread=check_same_thread
        )


    def drop(self):
        query = 'DROP TABLE address_book;'
        self.execute(query)


    def create(self):
        "주소록 테이블 생성"
        query = '''
        CREATE TABLE address_book(
            no           INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            first_name   TEXT    NOT NULL,
            last_name    TEXT    NOT NULL,
            email        TEXT        NULL,
            phone_no     TEXT        NULL,
            home_address TEXT        NULL,
            company      TEXT        NULL,
            description  TEXT        NULL
        );
        '''
        self.execute(query)


    def get(self, no):
        "주소록 조회"
        query = f'''
        SELECT * FROM address_book
        WHERE no = {no};
        '''
        data = self.fetch(query)
        result = Address(*data[0])
        return result


    def get_all(self):
        "주소록 전체 조회"
        query = 'SELECT * FROM address_book;'
        dataset = self.fetch(query)
        result = [Address(*data) for data in dataset]
        return result


    def add(self, address):
        "주소록 추가"
        query = f'''
        INSERT INTO address_book(
            first_name, last_name,
            email, phone_no,
            home_address, company,
            description
        ) VALUES (
            '{address.first_name}',
            '{address.last_name}',
            '{address.email}',
            '{address.phone_no}',
            '{address.home_address}',
            '{address.company}',
            '{address.description}'
        );
        '''
        self.execute(query)


    def update(self, no, address):
        "주소록 수정"
        query = f'''
        UPDATE address_book
        SET
            first_name   = '{address.first_name}',
            last_name    = '{address.last_name}',
            email        = '{address.email}',
            phone_no     = '{address.phone_no}',
            home_address = '{address.home_address}',
            company      = '{address.company}',
            description  = '{address.description}'
        WHERE no = {no};
        '''
        self.execute(query)


    def remove(self, no):
        "주소록 삭제"
        query = f'''
        DELETE FROM address_book
        WHERE no = {no};
        '''
        self.execute(query)


    def execute(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        cur.close()


    def fetch(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        result = cur.fetchall()
        cur.close()
        return result
