
import re

from urllib.request import urlopen
from urllib.parse import urljoin


url = 'https://www.google.com'
google = urlopen(url)
byte_stream = google.read()
html = byte_stream.decode('utf8')

pattern = re.compile(r'src="(.+?)"')
src = pattern.search(html)
url_logo = urljoin(url, src.group(1))
print(url_logo)

logo = urlopen(url_logo)
logo_byte_stream = logo.read()

with open('logo.png', 'wb') as file:
    file.write(logo_byte_stream)
