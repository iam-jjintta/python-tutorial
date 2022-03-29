'''
흔한 찐따의 파이썬 실행기
'''


import sys
import io


class stdio:
    "입출력 버퍼 재정의"

    def __init__(self):
        self._stdin = sys.stdin
        self._stdout = sys.stdout
        self._stderr = sys.stderr

        sys.stdin = io.StringIO()
        sys.stdout = io.StringIO()
        sys.stderr = io.StringIO()


    def close(self):
        sys.stdout.close()
        sys.stdin.close()
        sys.stderr.close()


class Executor:
    "파이썬 실행기"

    def __init__(self):
        if __name__ == '__main__':
            self.locals = __main__.__dict__
        else:
            self.locals = dict()
        self.stdio = stdio()


    @property
    def version(self):
        return '.'.join(map(str, sys.version_info[:3]))


    def runcode(self, code):
        try:
            exec(code, self.locals)
        except SystemExit as e:
            sys.stdout.write(f'SystemExit: {e}')
            self.stdio.close()
            sys.exit(0)
        except:
            try:
                sys.excepthook(*sys.exc_info())
            except:
                return sys.exc_info()
        finally:
            return self.flush()


    def flush(self):
        "호에에에엥"
        err = sys.stderr.getvalue()
        out = sys.stdout.getvalue()
        if err:
            sys.stderr.flush()
            return err
        else:
            sys.stdout.flush()
            return out

