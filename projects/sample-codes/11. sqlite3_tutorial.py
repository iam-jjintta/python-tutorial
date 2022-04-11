
# sqlite3: SQLite 데이터베이스용 DB-API 2.0 인터페이스
# SQLite는 별도의 서버 프로세스가 필요 없고 SQL 질의 언어의 비표준 변형을 사용한다.
# 데이터베이스에 액세스할 수 있는 경량 디스크 기반 데이터베이스를 제공하는 C 라이브러리이다.
# 일부 응용 프로그램은 내부 데이터 저장을 위해 SQLite를 사용할 수 있다.
# 자세한 내용은 파이썬 공식 문서의 "sqlite3 — SQLite 데이터베이스용 DB-API 2.0 인터페이스"를 참고하면 된다.
# 파이썬 sqlite3 공식 문서 링크: https://docs.python.org/ko/3/library/sqlite3.html
import sqlite3


# 데이터베이스를 생성한다.
con = sqlite3.connect('example.db')

# cursor 객체를 불러온다.
cur = con.cursor()

# 'stocks' 테이블을 생성한다.
cur.execute('''CREATE TABLE stocks
            (date text, trans text, symbol text, qty real, price real)
''')

# 'stocks' 테이블에 열 데이터를 추가한다.
cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# 'commit'을 통해 데이터를 저장한다.
con.commit()

# 데이터베이스와 연결이 완료되면 'close' 메서드를 통해 연결을 종료한다.
# 작업을 끝낸 후, 모든 변경 사항이 적용되었는지 확인해야 한다.
# 그렇지 않으면 'close' 메서드를 호출할 경우, 변경 내용이 손실된다.
con.close()
