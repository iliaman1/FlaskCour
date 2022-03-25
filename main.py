from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html', name='Ilia', title='Home page')


@app.route('/<float:num>/')
def x2(num):
    pi = 3.14
    return render_template('index.html', pi = pi, r = num)
    # return render_template('index.html', number=f"{float(num)}", text=f"Ваше число {float(num)}, умноженное на 2: {float(num)*2}")

@app.route('/filters/')
def tasks():
    numbers=(7, 5, 8, 0, 3)
    val='1.69'
    return render_template('filters.html', val=val, numbers=numbers)


# @app.route('/<int:a><oper><int:b>/')
# def calculate(a, b, oper):
#     operations = ('+', ':', '**', '-', '*')
#     if oper in operations and oper == '+':
#         return str(int(a) + int(b))
#     elif oper in operations and oper == ':':
#         return str(int(a) / int(b))
#     elif oper in operations and oper == '**':
#         return str(int(a) ** int(b))
#     elif oper in operations and oper == '-':
#         return str(int(a) - int(b))
#     elif oper in operations and oper == '*':
#         return str(int(a) * int(b))



if __name__ == '__main__':
    app.run(debug = True)