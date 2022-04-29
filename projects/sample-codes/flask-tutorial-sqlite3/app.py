
from database import Address
from database import AddressBook

from flask import Flask
from flask import request
from flask import render_template
from flask import redirect


db = AddressBook()
app = Flask(__name__)
app.secret_key = 'iamjjintta'


@app.before_first_request
def init_app():
    db.drop()
    db.create()


@app.route('/')
def main():
    title = 'Flask & SQLite3 Tutorial'
    books = db.get_all()
    template = render_template(
        'index.html',
        title=title,
        books=books
    )
    return template


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        title = 'Add AddressBook'
        template = render_template('add.html', title=title)
        return template

    elif request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        phone_no = request.form.get('phone_no')
        home_address = request.form.get('home_address')
        company = request.form.get('company')
        description = request.form.get('description')

        address = Address(
            0, first_name, last_name,
            email, phone_no,
            home_address, company,
            description
        )
        db.add(address)
        return redirect('/')


if __name__ == '__main__':
    host = 'localhost'
    port = 80

    app.run(host=host, port=port)
