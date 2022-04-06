
# requests: 파이썬용 HTTP 클라이언트 인터페이스를 위한 고수준 라이브러리
import requests

# urllib: URL 처리를 위한 파이썬 표준 라이브러리
from urllib.parse import urljoin
# html.parser: 간단한 HTML과 XHTML 구문 분석기를 위한 파이썬 표준 라이브러리
from html.parser import HTMLParser

# 구글 로고 이미지 URL 추출을 위한 'GoogleLogoHTMLParser' 클래스를 정의한다.
class GoogleLogoHTMLParser(HTMLParser):

    # 구글 로고의 img 태그의 속성들을 지정하기 위한 변수를 선언한다.
    attrs = None

    def handle_starttag(self, tag, attrs):
        # 태그가 img 태그일 경우에 attrs 변수에 태그 속성들을 지정한다.
        if tag == 'img':
            for attr, value in attrs:
                # 구글 로고에 해당하는 alt 속성이 'Google'이다.
                if attr == 'alt' and value == 'Google':
                    self.attrs = attrs
                    break


url = 'https://www.google.com'
google = requests.get(url)
html = google.text

parser = GoogleLogoHTMLParser()
parser.feed(html)

for attr, value in parser.attrs:
    if attr == 'src':
        url_logo = urljoin(url, value)
        logo = requests.get(url_logo)

        byte_stream = logo.content
        with open('logo.png', 'wb') as file:
            file.write(byte_stream)

        break
