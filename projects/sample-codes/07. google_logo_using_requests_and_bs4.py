
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
html = google.text

# html.parser 라이브러리와 html5lib, 그리고 lxml 라이브러리에 있는 파서(parser)들을 사용할 수 있다.
# 가능하다면, 속도를 위해 lxml 라이브러리를 설치해 사용하는 것을 권장한다고 한다.
# 구버전의 파이썬을 사용한다면 lxml 라이브러리를 사용하는 것이 필수라고 한다.
# 그렇지 않고 구버전의 파이썬 내장 HTML 해석기 html5lib 라이브러리는 별로 좋지 않다고 한다.
# 다만, 복잡한 HTML 문서같은 경우(특히 HTML 문서의 태그가 엉망인 경우)에는 html.parser 혹은 html5lib 라이브러리를 고려해볼만 하다.
# 즉, 결론은 lxml 라이브러리는 속도와 성능면에서 굉장히 우수하기 때문에 lxml 라이브러리를 사용하는 것이 좋다.
parser = BeautifulSoup(html, 'lxml')

# lxml과 마찬가지로 XPath 혹은 CSS Selector 문법을 통해 태그를 가져올 수 있다.
# CSS Selector 문법은 XPath보다 훨씬 더 쉽고 속도와 성능이 더 뛰어나다고 한다.
# 그러나 CSS Selector는 태그의 속성으로만 검색이 가능하다.
# 따라서 단순히 HTML 문서에서 텍스트만으로 태그를 검색하려면 XPath를 사용해야 한다.
# 하지만 대부분의 HTML 문서에는 태그의 id를 사용하는 것이 일반적이다.
# 고로 CSS Selector를 사용하는 편이 문법적으로도 쉽고 성능도 더 좋기 때문에 XPath보다 더 권장되는 방식이다.
# CSS Selector를 사용하여 태그를 찾기 위해서는 'select' 메서드나 'find_all' 메서드를 사용하면 된다.
# 태그를 하나만 가져오려면 'select_one' 메서드나 'find' 메서드를 통해 가져올 수 있다.
img_tags = parser.find_all('img')

for tag in img_tags:
    # dict 타입처럼 Key 인덱싱을 통해 태그의 속성값을 가져올 수 있다.
    src = tag['src']
    url_logo = urljoin(url, src)
    google_logo = requests.get(url_logo)
    byte_stream = google_logo.content

    filename = src.split('/')[-1]
    with open(filename) as file:
        file.write(byte_stream)
