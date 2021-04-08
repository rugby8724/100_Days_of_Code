from flask import Flask
app = Flask(__name__)


def bold_decorator(function):
    def wrapper():
        return '<b>' + function + '<b>'


@app.route('/')
def hello_world():
    return 'Hello, World'


@app.route('/bye')
@bold_decorator
def bye():
    return 'Bye'

@app.route('/<name>/<int:number>')
def greet(name, number):
    return f'Hello {name}, you are {number} years old!'


if __name__ == '__main__':
    #Run the app in debug mode to auto-reload
    app.run(debug=True)