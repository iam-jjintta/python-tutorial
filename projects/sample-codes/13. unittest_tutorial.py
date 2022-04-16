
# unittest: 단위 테스트 프레임워크
# 파이썬 표준 라이브러리 공식 문서: https://docs.python.org/ko/3/library/unittest.html
# unittest 단위 테스트 프레임워크는 본래 JUnit으로부터 영감을 받고 다른 언어의 주요 단위 테스트 프레임워크와 비슷한 특징을 가지고 있다.
# 이것은 테스트 자동화, 테스트를 위한 사전 설정(setup)과 종료(shutdown) 코드 공유, 테스트를 컬렉션에 종합하기, 테스트와 리포트 프레임워크의 분리 등을 지원한다.
import unittest


# unittest 모듈은 테스트를 구성하고 실행하는 데 풍부한 도구 모음을 제공하고 있다.
# 아래의 예시 코드는 https://docs.python.org/ko/3/library/unittest.html#basic-example 에서 확인할 수 있다.
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
