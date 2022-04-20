
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def main():
    title = 'Flask Tutorial'
    message = 'Hello, Flask!'
    template = render_template('example.html', title=title, message=message)
    return template


if __name__ == '__main__':
    host = 'localhost'
    port = 80

    app.run(host=host, port=port)
