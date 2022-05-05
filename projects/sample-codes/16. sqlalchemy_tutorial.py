
# SQLAlchemy: 파이썬 SQL 개발 도구 및 객체 관계형 매퍼(ORM; Object Relational Mapper)
# SQLAlchemy는 응용 프로그램 개발자에게 SQL의 모든 기능과 유연성을 제공하는 파이썬 SQL 도구 키트 및 개체 관계형 매퍼이다.
# SQLAlchemy는 간단하고 파이쏘닉(Pythonic)한 도메인 언어에 맞게 조정되어 효율적이다.
# 또한, 고성능 데이터베이스 액세스를 위해 설계된 잘 알려진 엔터프라이즈 수준 지속성 패턴의 전체 제품군을 제공한다.
# SQLAlchemy는 데이터 매퍼 패턴 을 제공하는 선택적 구성 요소인 객체 관계형 매퍼(ORM)로 가장 유명하다.
# 여기서 클래스는 개방형 다중 방식으로 데이터베이스에 매핑될 수 있으므로 객체 모델과 데이터베이스 스키마가 처음부터 깔끔하게 분리되었다.
# SQLAlchemy를 사용하기 위해서는 명령 프롬프트에 'pip' 명령어를 통해 설치해야 한다.
# 설치 명령어: pip install SQLAlchemy

# 데이터베이스의 테이블(Table)을 생성하기 위해서는 다음과 같이 테이블의 컬럼(Column) 객체를 import 한다.
# 또한, 다음과 같이 각 컬럼에 해당하는 데이터 타입 객체들을 import 한다.
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text
# 'create_engine'은 데이터베이스 엔진을 생성하는 함수이다.
from sqlalchemy import create_engine

# ORM을 사용하기 위해 다음과 같이 세션(Session) 객체를 import 한다.
# ORM이란, Object Relational Mapping 즉, 객체-관계 매핑의 줄임말이다.
# 객체-관계 매핑을 풀어서 설명하자면 OOP(Object Oriented Programming)에서 쓰이는 객체라는 개념을 구현한 클래스와
# RDB(Relational DataBase)에서 쓰이는 데이터인 테이블 자동으로 매핑(연결)하는 것을 의미한다.
# 그러나 클래스와 테이블은 서로가 기존부터 호환가능성을 두고 만들어진 것이 아니기 때문에 불일치가 발생하는데,
# 이를 ORM을 통해 객체 간의 관계를 바탕으로 SQL문을 자동으로 생성하여 불일치를 해결한다.
# 따라서 ORM을 이용하면 따로 SQL문을 짤 필요없이 객체를 통해 간접적으로 데이터베이스를 조작할 수 있게 된다.
from sqlalchemy.orm import Session
# 'declarative_base' 함수는 ORM 기본(base) 객체를 정의하기 위한 함수이다.
from sqlalchemy.orm import declarative_base


# 사용할 데이터베이스를 정의한다.
# 여기서는 SQLite를 사용하기 위해 다음과 같이 'sqlite:///'를 사용했다.
db = 'sqlite:///test.db'
# 데이터베이스 엔진을 생성한다.
engine = create_engine(db, echo=True, future=True)
# ORM 기본(base) 객체를 정의하기 위해 Base 객체를 생성한다.
Base = declarative_base()


# ORM 클래스를 정의한다.
class Test(Base):
    # 테이블명은 '__tablename__'으로 정의한다.
    __tablename__ = 'Test'

    # 테이블 컬럼을 정의한다.
    no = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    data = Column(Text, nullable=True)


    def __init__(self, data=None):
        self.data = data


    # 관례적으로 '__repr__' 함수를 재정의한다.
    def __repr__(self):
        return f'Test(no={self.no!r}, data={self.data!r})'


# 테이블 설정을 완료하면 스키마를 생성한다.
# 아래와 같이 메타 데이터를 보관하고 있는 'Base'를 이용해 스키마를 간단하게 생성해줄 수 있다.
Base.metadata.create_all(engine)


# 데이터를 추가하는 함수 'add' 정의
def add(test):
    # 세션(Session) 객체를 통해 데이터베이스 엔진(engine)에 연결한다.
    with Session(engine) as session:
        test = Test('SQLAlchemy Tutorial')
        # 세션(Session) 객체의 'add' 메서드를 통해 데이터를 추가한다.
        session.add(test)
        # 새로운 데이터 추가 후 커밋(commit)을 해준다.
        session.commit()


# 데이터를 조회하는 함수 'get' 정의
def get(no=None):
    with Session(engine) as session:
        # 세션(Session) 객체를 통해 쿼리문(SQL)을 정의한다.
        query = session.query(Test)
        # 'no'가 'None'이 아닐 경우, 테이블 'Test'의 'no'와 일치하는 데이터를 조회하는 쿼리문을 만든다.
        if no is not None:
            query = query.filter(Test.no == no)
        # 'no'를 기준으로 정렬한다.
        query = query.order_by(Test.no)
        # 테이블 'Test'의 데이터를 모두 조회한다.
        result = query.all()
        return result


if __name__ == '__main__':
    test = Test('SQLAlchemy Tutorial')
    add(test)

    result_all = get()
    print(result_all)

    result = get(1)
    print(result[0])
