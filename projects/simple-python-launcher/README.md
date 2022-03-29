
# 흔한 찐따의 파이썬 GUI 런처
파이썬으로 메모장을 만들었고, 그 파이썬으로 만든 메모장으로 파이썬 런처(실행기)를 만들었습니다.

이 파이썬으로 만든 메모장으로 만든 실행기로 만든 파이썬 코드를 실행해본 결과입니다.
(뭔가 난해한 거 같은데.. 딱히 다른 방법으로 설명할 방법이 안 떠오르네요..)

이제는 단순한 메모장이 아니라, 엄연한 파이썬 코드 실행기가 되었습니다.

## 사용한 라이브러리
사용한 라이브러리는 저번에 사용했던 거랑 동일합니다.

새로 추가하거나 사용하지 않은 라이브러리는 없습니다.

- [tkinter — Tcl/Tk 파이썬 인터페이스](https://docs.python.org/ko/3/library/tkinter.html)
- [sys — 시스템 특정 파라미터와 함수](https://docs.python.org/ko/3/library/sys.html)
- [webbrowser — Convenient web-browser controller](https://docs.python.org/ko/3/library/webbrowser.html)

## 추가된 기능
새롭게 추가한 기능들은 다음과 같습니다.
- 파일 열기 시 `.py` 파일 확장자 구분 기능
- 파이썬 코드 실행 기능
- *exception hook* 메시지 출력 기능
- 텍스트 줌인, 줌아웃 기능
- `Tab` 키 입력 시 공백 문자 4번으로 치환 기능

## 실행 결과
![실행 결과]()