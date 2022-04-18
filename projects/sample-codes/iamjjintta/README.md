# 흔한 찐따의 PyPI에 파이썬 패키지 베포하기

## 준비하기
먼저, 아래처럼 `pip` 명령어를 통해 파이썬에서 기본적으로 제공하는 `setuptools` 라이브러리를 업데이트 해준다.
```sh
pip install -U setuptools
```

그 다음, `pip` 명령어를 통해 다음과 같이 `wheel` 모듈을 설치한다.

```sh
pip install wheel
```

## 빌드하기
패키지를 빌드하려면 다음과 같이 명령어를 입력한다.

```sh
python setup.py bdist_wheel
```

그러나, 배포를 위한 모듈인 `twine` 에서는 `sdist` 옵션을 사용하도록 예시로 설명하고 있다.
그래서 다음과 같이 `sdist` 옵션을 사용했다.

```sh
python setup.py sdist bdist_wheel
```

## 배포하기
[PyPI](https://pypi.org/)에 배포를 하기 위해서는 다음과 같이 `pip` 명령어를 통해 `twine` 모듈을 설치한다.

```sh
pip install twine
```

[PyPI](https://pypi.org/)에서 회원 가입을 한 후, 다음과 같이 명령어를 입력한다.

```sh
twine upload dist/*
```

이렇게 하면 배포가 완료된다.

## 확인하기
내가 배포한 파이썬 패키지를 확인하려면 `pip` 명령어를 통해 배포한 패키지를 설치해본다.
나는 `iamjjintta` 라는 이름의 패키지를 배포하였다.

```sh
pip install iamjjintta
```

성공적으로 패키지가 다운로드 되었다면 자신이 배포한 파이썬 패키지를 사용할 수 있다.

```python
from iamjjintta import iamjjintta

iamjjintta.open_blog()
```
