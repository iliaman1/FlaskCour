from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/contact/')
def contact():
    return 'contact information'

@app.route('/calculate/<a>/<b>/')
def calculate(a, b):
    return str(int(a)**int(b))


if __name__ == '__main__':
    app.run(debug = True)