
# Pillow: 광범위한 파일 형식 지원, 효율적인 내부 표현 및 강력한 이미지 처리 기능을 제공하는 라이브러리
# 파이썬 이미지 처리를 위한 라이브러리이며, 파이썬 인터프리터에 이미지 처리 기능을 추가한다.
# 핵심 이미지 라이브러리이며, 몇 가지 기본 픽셀 형식으로 저장된 데이터에 빠르게 액세스할 수 있도록 설계되었다.
# 사용하기 위해서는 명령 프롬프트에 'pip' 명령어를 통해 설치해야 한다.
# 설치 명령어: pip install Pillow
from PIL import Image

# Image 클래스의 open 함수를 통해 이미지 파일을 쉽게 불러올 수 있다.
image = Image.open('test.png')
# 이미지 포맷, 이미지 크기, 이미지 픽셀 유형
print(image.format, image.size, image.mode)
# 이미지 파일을 컴퓨터에 지정된 기본 이미지 뷰어로 이미지를 연다.
image.show()
