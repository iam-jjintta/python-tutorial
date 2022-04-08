
# requests: 파이썬용 HTTP 클라이언트 인터페이스를 위한 고수준 라이브러리
import requests


# urllib: URL 처리를 위한 파이썬 표준 라이브러리
from urllib.parse import urljoin

# bs4: HTML 및 XML 문서에서 데이터를 가져오기 위한 파이썬 라이브러리
# html.parser 라이브러리와 lxml 라이브러리의 파싱(parsing) 기능을 사용할 수 있다.
# bs4 라이브러리를 사용하기 위해서는 명령 프롬프트에서 'pip' 명령어를 통해 설치하면 된다.
# 설치 명령어: pip install bs4
from bs4 import BeautifulSoup


url = 'https://www.google.com'
google = requests.get(url)

# lxml 패키지에 있는 파서(parser)를 사용할 수 있다.
parser = BeautifulSoup(google.text, 'lxml')

# lxml과 마찬가지로 XPath 혹은 CSS Selector 문법을 통해 태그를 가져올 수 있다.
# CSS Selector 문법은 XPath보다 성능이 더 좋다고 한다.
img_tags = parser.findall('img')

for tag in img_tags:
    # dict 타입처럼 Key 인덱싱을 통해 태그의 속성값을 가져올 수 있다.
    src = tag['src']
    url_logo = urljoin(url, src)
    google_logo = requests.get(url_logo)
    byte_stream = google_logo.content

    filename = src.split('/')[-1]
    with open(filename) as file:
        file.write(byte_stream)
