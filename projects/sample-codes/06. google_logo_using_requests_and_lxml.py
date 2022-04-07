
# requests: 파이썬용 HTTP 클라이언트 인터페이스를 위한 고수준 라이브러리
import requests

# urllib: URL 처리를 위한 파이썬 표준 라이브러리
from urllib.parse import urljoin

# lxml: XML 및 HTML 문서의 빠른 처리를 위한 라이브러리
# 속도가 굉장히 빠르며, XML 및 HTML 문서의 구문 분석 중에 잘못된 태그를 처리해주기도 한다.
# lxml 라이브러리를 사용하기 위해서는 명령 프롬프트에 'pip' 명령어를 통해 설치하면 된다.
# 설치 명령어: pip install lxml
from lxml import html


url = 'https://www.google.com'
google = requests.get(url)
# str 타입인 text 보다는 암묵적으로 bytes 타입인 content를 받도록 하는 것이 좋다고 한다.
# 그 이유는 잘 모르겠으나, 개인적인 생각에는 아마도 속도와 성능 차이때문인 것으로 추정된다.
# (이것은 어디까지나 나의 개인적인 생각이다.)
# str은 유니코드(Unicode)이며, 하나의 UTF-8 문자를 표현하는데 2 bytes, 즉 16 bit이다.
# 반면, bytes는 하나의 ASCII 문자를 표현하는데 1 bytes, 즉 8 bit이다.
document = html.fromstring(google.content)

# HTML 문서에서 원하는 태그를 찾기 위해서는 XPath 문법을 사용해야 한다.
# XPath 문법 중 './/태그명'을 사용하면 모든 태그에 포함된 요소를 의미한다.
# 즉, './/img' 라고 하면 HTML 문서에 있는 모든 'img' 태그를 가져온다.
# xpath 메서드 혹은 findall 메서드를 통해 태그를 찾는다.
img_tags = document.findall('.//img')
for img in img_tags:
    src = img.get('src')
    url_logo = urljoin(url, src)

    google_logo = requests.get(url_logo)
    byte_stream = google_logo.content

    filename = src.split('/')[-1]
    with open(filename, 'wb') as file:
        file.write(byte_stream)
