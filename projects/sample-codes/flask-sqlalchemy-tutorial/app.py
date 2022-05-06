
# Flask: 파이썬용 마이크로 프레임워크
from flask import Flask
from flask import request

from flask import render_template
from flask import url_for
from flask import redirect

# Flask-SQLAlchemy: Flask 프레임워크에 대한 SQLAlchemy 라이브러리 지원을 추가하는 Flask 프레임워크의 확장 라이브러리
# Flask-SQLAlchemy 라이브러리는 일반적인 작업을 쉽게 수행할 수 있도록 유용한 기본값과 추가 도우미를 제공한다.
# Flask-SQLAlchemy 라이브러리는 Flask 프레임워크와 함께 SQLAlchemy 라이브러리 사용의 단순화를 목표로 한다.
# 또한, SQLAlchemy 라이브러리에서 지원하는 ORM으로 작업하는 방법 역시 지원한다.
# Flask-SQLAlchemy 라이브러리를 사용하기 위해서는 명령 프롬프트에 'pip' 명령어를 입력해야 한다.
# 설치 명령어: pip install Flask-SQLAlchemy

# ORM을 사용하기 위해서는 다음과 같이 flask_sqlalchemy 라이브러리 안의 SQLAlchemy 객체를 import 한다.
from flask_sqlalchemy import SQLAlchemy


# 데이터베이스를 정의한다.
db = 'sqlite:///DataTable.db'
# Flask-SQLAlchemy에서 제공하는 ORM을 정의한다.
orm = SQLAlchemy()

app = Flask(__name__)
# Flask 애플리케이션 설정에서 데이터베이스 경로를 지정한다.
app.config['SQLALCHEMY_DATABASE_URI'] = db


# ORM을 정의하는 방법은 SQLAlchemy 라이브러리와 동일하다.
# SQLAlchemy 객체의 클래스 'Model'을 상속받아서 ORM 객체를 정의한다.
class DataTable(orm.Model):
    # SQLAlchemy 라이브러리처럼 테이블명은 '__tablename__'에 정의한다.
    # 만약 정의하지 않는다면 정의된 ORM 클래스명으로 정의된다.
    __tablename__ = 'data_table'

    # SQLAlchemy 라이브러리 사용법과 동일하게 데이터의 컬럼을 정의한다.
    no = orm.Column(orm.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = orm.Column(orm.Text, nullable=False)
    description = orm.Column(orm.Text, nullable=True)


    # 마찬가지로, 관례적으로 특수 메서드 '__repr__'을 재정의한다.
    def __repr__(self):
        return f'<DataTable {self.name!r}>'


# Flask 애플리케이션이 실행된 후, 최초로 요청을 보내면 데이터베이스 초기화 작업을 진행한다.
@app.before_first_request
def init():
    # 'init_app' 메서드를 통해 데이터베이스 설정과 함께 사용할 Flask 애플리케이션을 초기화한다.
    orm.init_app(app)
    # 'create_all' 메서드를 통해 테이블과 데이터베이스를 생성한다.
    orm.create_all()


@app.route('/')
def main():
    title = 'Flask SQLAlchemy Tutorial'
    data_table = DataTable.query.all()
    template = render_template(
        'index.html',
        title=title,
        data_table=data_table
    )
    return template


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        title = 'Add Data'
        template = render_template('add.html', title=title)

    elif request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        data = DataTable(name=name, description=description)

        # SQLAlchemy 라이브러리와 동일하게 세션(Session) 객체를 통해서 데이터베이스에 접근하여 작업한다.
        orm.session.add(data)
        orm.session.commit()

        url = url_for('main')
        template = redirect(url)

    return template


if __name__ == '__main__':
    host = 'localhost'
    port = 80

    app.run(host=host, port=port)
