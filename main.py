from flask import Flask

operations = ('+', ':', '**', '-', '*')
app = Flask(__name__)


@app.route('/<int:a><oper><int:b>/')
def calculate(a, b, oper):
    if oper in operations and oper == '+':
        return str(int(a) + int(b))
    elif oper in operations and oper == ':':
        return str(int(a) / int(b))
    elif oper in operations and oper == '**':
        return str(int(a) ** int(b))
    elif oper in operations and oper == '-':
        return str(int(a) - int(b))
    elif oper in operations and oper == '*':
        return str(int(a) * int(b))


if __name__ == '__main__':
    app.run(debug = True)