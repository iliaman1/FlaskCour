from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'dobri pa4antak'


if __name__ == '__main__':
    app.run(debug = True)