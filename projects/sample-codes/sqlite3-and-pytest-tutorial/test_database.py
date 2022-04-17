'''
[결과]
(venv) C:\Users\iamjjintta\study>pytest -v test_database.py
================================================= test session starts =================================================
platform win32 -- Python 3.10.4, pytest-7.1.1, pluggy-1.0.0 -- C:\Users\iamjjintta\study\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\iamjjintta\study
collected 6 items

test_database.py::test_테이블_생성 PASSED                                                                     [ 16%]
test_database.py::test_데이터_삽입 PASSED                                                                     [ 33%]
test_database.py::test_데이터_전체_조회 PASSED                                                                [ 50%]
test_database.py::test_데이터_조회 PASSED                                                                     [ 66%]
test_database.py::test_데이터_수정 PASSED                                                                     [ 83%]
test_database.py::test_데이터_삭제 PASSED                                                                     [100%]

================================================== 6 passed in 0.57s ==================================================
'''


from db.database import Database
from db.database import Test

# 논리적/다목적 설계를 위한 프로그래밍을 진행하는 것이 아닌,
# 단순히 기능이 잘 동작하는지 여부에 대한 단위 테스트를 진행하는 것이므로
# 어떤 기능에 대한 테스트인지 한눈에 알아볼 수 있도록
# 아래와 같이 함수명을 한글로 타이핑 하였다.

def 데이터베이스_연결():
    db = Database()
    return db


def test_테이블_생성():
    db = 데이터베이스_연결()
    result = db.create()
    assert result


def test_데이터_삽입():
    db = 데이터베이스_연결()
    test = Test('테스트1', '테스트2')
    result = db.add(test)
    assert result


def test_데이터_전체_조회():
    db = 데이터베이스_연결()
    result = db.get_all()
    assert result == ((1, '테스트1', '테스트2'),)


def test_데이터_조회():
    db = 데이터베이스_연결()
    where = 1
    result = db.get(where)
    assert result == (where, '테스트1', '테스트2')


def test_데이터_수정():
    db = 데이터베이스_연결()
    where = 1
    test = Test('테스트3', '테스트4')
    result = db.edit(where, test)
    assert result


def test_데이터_삭제():
    db = 데이터베이스_연결()
    where = 1
    result = db.remove(where)
    assert result
