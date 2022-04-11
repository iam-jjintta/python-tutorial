
# sqlite3: SQLite 데이터베이스용 DB-API 2.0 인터페이스
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
