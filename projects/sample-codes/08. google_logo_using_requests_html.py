
# urllib: URL 처리를 위한 파이썬 표준 라이브러리
from urllib.parse import urljoin

# requests_html: HTML 구문 분석을 최대한 간단하고 직관적으로 개발된 파이썬 라이브러리
# requests_html은 requests 라이브러리를 개발한 공식 PSF(파이썬 소프트웨어 재단)에서 확장해서 개발한 라이브러리이다.
# requests의 확장된 라이브러리라서 그런지 XPath와 CSS Selector, Javascript 분석 또한 지원한다.
# requests_html 라이브러리를 사용하기 위해서는 명령 프롬프트에 'pip' 명령어를 통해 설치해야 한다.
# 설치 명령어: pip install requests_html
from requests_html import HTMLSession


url = 'https://www.google.com'

# 사용하기 위해서는 먼저 HTMLSession 객체를 생성한다.
session = HTMLSession()
google = session.get(url)

# HTML 문서는 html 프로퍼티에 HTML 객체로 생성되어 있다.
html = google.html
# 그 다음, find 메서드를 통해 CSS Selector 문법으로 태그를 찾아낼 수 있다.
# 만약 XPath로 찾고자 하는 경우에는 xpah 메서드를 사용하면 된다.
img_tags = html.find('img')

for tag in img_tags:
    # 태그의 속성은 attrs 프로퍼티에 정의되어 있으며, dict 타입이다.
    # attrs는 dict 타입이므로, Key 인덱싱을 통해서 태그의 속성값을 가져올 수 있다.
    src = tag.attrs['src']
    url_logo = urljoin(url, src)
    google_logo = session.get(url_logo)
    byte_stream = google_logo.content

    filename = src.split('/')[-1]
    with open(filename, 'wb') as file:
        file.write(byte_stream)
