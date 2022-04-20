
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def main():
    title = '펭귄의 귀여움'
    name = '펭귄'
    description = '펭귄은 지구상에서 가장 귀여운 생명체입니다.'

    template = render_template(
        'example.html',
        title=title,
        name=name,
        description=description
    )
    return template


if __name__ == '__main__':
    host = 'localhost'
    port = 80

    app.run(host=host, port=port)
