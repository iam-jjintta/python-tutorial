
# sqlite3: SQLite 데이터베이스용 DB-API 2.0 인터페이스
import sqlite3

# 주소록 아이템 클래스 정의
class Address:
    '''
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
        first_name, last_name,
        email=None, phone_no=None,
        home_address=None, company=None,
        description=None
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_no = phone_no
        self.home_address = home_address
        self.company = company
        self.description = description


# 주소록 클래스 정의
class AddressBook:

    def __init__(self):
        self.conn = sqlite3.connect('address_book.db')


    def create(self):
        "주소록 테이블 생성"
        query = '''
        CREATE TABLE address_book(
            no INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NULL,
            phone_no TEXT NULL,
            home_address TEXT NULL,
            company TEXT NULL,
            description TEXT NULL
        );
        '''
        self.execute(query)


    def get(self, no):
        "주소록 조회"
        query = f'''
        SELECT * FROM address_book
        WHERE no = {no};
        '''
        result = self.fetch(query)[0]
        return result


    def get_all(self):
        "주소록 전체 조회"
        query = 'SELECT * FROM address_book;'
        result = self.fetch(query)
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
            first_name = '{address.first_name}',
            last_name = '{address.last_name}',
            email = '{address.email}',
            phone_no = '{address.phone_no}',
            home_address = '{address.home_address}',
            company = '{address.company}',
            description = '{address.description}'
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
        with self.conn.cursor() as cur:
            cur.execute(query)
            self.conn.commit()


    def fetch(self, query):
        with self.conn.cursor() as cur:
            cur.execute(query)
            result = cur.fetchall()
        return result


if __name__ == '__main__':
    addr_book = AddressBook()
    addr_book.create()

    addr = Address(
        '흔한', '찐따',
        'iamjjintta@gmail.com',
        '010-1234-5678',
        '방구석',
        '찐따 격리소',
        '나는 찐따다.'
    )
    addr_book.add(addr)

    result = addr_book.get(1)
    result_all = addr_book.get_all()
    print(result)
    print(result_all)

    addr.first_name = '안 흔한'
    addr_book.update(1, addr)

    result_all = addr_book.get_all()
    print(result_all)

    addr_book.remove(1)

    result_all = addr_book.get_all()
    print(result_all)
