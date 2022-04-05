
# re: 정규식을 위한 파이썬 표준 라이브러리
import re
# requests: 파이썬 HTTP 처리를 위한 고수준 라이브러리
# 파이썬 공식 문서에 따르면, urllib 라이브러리 대신 requests 라이브러리를 사용할 것을 권장하고 있다.
# 사용하기 위해서는 'pip' 명령어를 통해 패키지를 설치한 다음 사용하면 된다.
# 설치 명령어: pip install requests
import requests

# urllib: URL 처리를 위한 파이썬 표준 라이브러리
from urllib.parse import urljoin


url = 'https://www.google.com'
# 'get' 함수를 통해 GET 방식으로 url을 요청한다.
# GET 방식이란, 'url?파라미터1=값1&파라미터2=값2&...' 형식으로 웹 서버에 HTML 문서를 요청하는 방식을 의미한다.
google = requests.get(url)
# 응답받은 Response 객체에서 'text' 프로퍼티에 접근하면 해당 URL의 HTML 문서를 가져올 수 있다.
html = google.text

# 정규식을 사용하여 구글 페이지 로고의 URL을 탐색한다.
pattern = re.compile(r'src="(.+?)"')
src = pattern.search(html)
url_img = src.group(1)

# 구글 도메인과 구글 페이지 로고의 URL을 합쳐준다.
url_logo = urljoin(url, url_img)
logo = requests.get(url_logo)

# Byte Stream 데이터는 'content' 프로퍼티를 통해 접근할 수 있다.
byte_stream = logo.content

# 받아온 이미지 데이터를 'logo.png' 이미지 파일로 저장시킨다.
with open('logo.png', 'wb') as file:
    file.write(byte_stream)
