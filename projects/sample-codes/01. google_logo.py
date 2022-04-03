
# re: 정규식을 위한 파이썬 표준 라이브러리
import re

# urllib: URL 처리를 위한 파이썬 표준 라이브러리
from urllib.request import urlopen
from urllib.parse import urljoin


# 구글 페이지로 접속하여 HTML 코드를 받아온다.
url = 'https://www.google.com'
google = urlopen(url)

# 바이트 스트림 데이터를 불러온 후, UTF-8 형식으로 변환해준다.
byte_stream = google.read()
html = byte_stream.decode('utf8')

# 정규식을 사용하여 구글 페이지 로고의 URL을 탐색한다.
pattern = re.compile(r'src="(.+?)"')
src = pattern.search(html)
url_img = src.group(1)

# 구글 페이지 로고의 URL과 구글 도메인을 합쳐준 후에 로고 이미지에 접속한다.
url_logo = urljoin(url, url_img)
logo = urlopen(url_logo)

# 이미지 데이터, 즉 바이트 스트림을 받아온다.
logo_byte_stream = logo.read()

# 받아온 이미지 데이터를 이미지 파일로 저장시킨다.
with open('logo.png', 'wb') as file:
    file.write(logo_byte_stream)
