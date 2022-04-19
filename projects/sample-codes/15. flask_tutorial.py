
# flask: Python용 "마이크로 프레임워크(micro-framework)"이다.
# flask는 더 작은 애플리케이션, API 및 웹 서비스를 구축하기 위한 라이브러리이다.
# 디자인 패턴 중에서 웹 프레임워크에 보편적으로 사용되는 패턴인 'MVC 패턴'으로 설계되었다.
# flask는 특히 간단하게 웹 서비스를 개발할 수 있는 강력한 프레임워크이다.
# flask를 사용하기 위해서는 명령 프롬프트에 'pip' 명령어를 통해 설치해야 한다.
# 설치 명령어: pip install flask
from flask import Flask


# 먼저, Flask 애플리케이션 객체를 생성한다.
# Flask 객체는 웹 애플리케이션을 구현하고 그 중심적인 역할을 한다.
# 인자값으로 애플리케이션의 모듈 또는 패키지 이름이 전달된다.
# 일단 생성되면 보기(View) 기능, URL 규칙(rules), 템플릿(templates) 구성 등을 위한 애플리케이션의 중심부 역할을 한다.
app = Flask(__name__)


# 그 다음 'route' 함수를 통해 URL을 지정한다.
# 아래의 예시러럼 데코레이터로 정의한다.
@app.route('/')
def main():
    # 반환값은 웹 브라우저에 보여주기 위한 HTML 코드가 전달된다.
    return '<h1>Hello, Flask!</h1>'


# Flask 애플리케이션을 실행하기 위해서는 'run' 메서드를 호출하면 된다.
# 인자값으로는 호스트(host) 주소와 포트(port) 번호를 받는다.
# 여기서는 포트 번호를 웹 서버 포트 번호인 '80'을 입력해주었다.
if __name__ == '__main__':
    host = 'localhost'
    port = 80

    app.run(host, port)

# 실행이 완료되면 http://localhost:80 으로 접속해본다.
# URL 뒷부분의 포트 번호는 웹 포트 번호인 80이므로,
# http://localhost 같이 생략하여 접속이 가능하다.
