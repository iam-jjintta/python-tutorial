
# html.parser: 간단한 HTML과 XHTML 구문 분석기를 위한 파이썬 표준 라이브러리
from html.parser import HTMLParser


# HTML로부터 Tag와 Data를 출력하는 'MyHTMLParser' 클래스를 정의한다.
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("시작 태그:", tag)

    def handle_endtag(self, tag):
        print("종료 태그:", tag)

    def handle_data(self, data):
        print("데이터:", data)


# 테스트를 위한 HTML 문서를 정의한다.
html = '''
<html>
<head>
    <title>Test</title>
</head>
<body>
    <h1>흔한 찐따의 HTML 구문 분석</h1>
    <p>안녕하세요, 흔한 찐따입니다.</p>
    <p>만나서 반갑습니다.</p>
    <p>이것은 파이썬 HTML 구문 분석 테스트입니다.</p>
</body>
</html>
'''

# HTMLParser 객체를 생성한다.
parser = MyHTMLParser()

# HTML 문서의 구문을 분석한 후에 결과를 출력시킨다.
parser.feed(html)
