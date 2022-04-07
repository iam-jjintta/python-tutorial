
# requests: 파이썬용 HTTP 클라이언트 인터페이스를 위한 고수준 라이브러리
import requests

# html5lib: HTML 파싱(parsing)을 위한 순수 파이썬 라이브러리
# 모든 주요 웹 브라우저에서 구현되는 WHATWG HTML 사양을 준수하도록 설계되었다.
# html5lib 라이브러리를 사용하기 위해서는 명령 프롬프트에 'pip' 명령어를 통해 설치하면 된다.
# 설치 명령어: pip install html5lib
import html5lib

# urllib: URL 처리를 위한 파이썬 표준 라이브러리
from urllib.parse import urljoin


url = 'https://www.google.com'
google = requests.get(url)
html = google.text

# html5lib 라이브러리의 parse 함수를 통해 HTML 태그와 데이터를 파싱한다.
# 이때, treebuilder의 인자값으로 'dom'을 넘겨주면 트리 형태의 구조로 가져온다.
document = html5lib.parse(html, treebuilder='dom')
# getElementsByTagName 메서드를 통해 해당하는 모든 태그들을 가져온다.
img_tags = document.getElementsByTagName('img')
for tag in img_tags:
    # getAttribute 메서드를 통해 태그의 속성을 가져온다.
    src = tag.getAttribute('src')

    # HTML 문서에 정의되어 있는 모든 img 태그의 이미지들을 저장시킨다.
    url_img = urljoin(url, src)
    google_logo = requests.get(url_img)
    byte_stream = google_logo.content

    # src 속성에는 '.../url_경로/이미지_파일명.확장자' 구조로 되어있다.
    # 때문에 '/'의 맨 마지막 부분이 이미지 파일명에 해당된다.
    filename = src.split('/')[-1]
    # 해당 파일명으로 이미지 파일을 저장시킨다.
    with open(filename, 'wb') as file:
        file.write(byte_stream)
