from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html', name='Ilia', title='Home page')


@app.route('/<float:num>/')
def x2(num):
    pi = 3.14
    return render_template('index.html', pi=pi, r=num)
    # return render_template('index.html', number=f"{float(num)}", text=f"Ваше число {float(num)}, умноженное на 2: {float(num)*2}")


@app.route('/filters/')
def tasks():
    numbers = (7, 5, 8, 0, 3)
    val = '1.69'
    return render_template('filters.html', val=val, numbers=numbers)


@app.route('/sintif/')
@app.route('/<float:a>/<oper>/<float:b>/')
def sintask(a, oper, b):
    operations = ('+', ':', '**', '-', '*')
    a1, b1, c1 = 1, 2, 3
    return render_template('jinja_if.html', a=a, oper=oper, b=b, operations=operations, a1=a1, b1=b1, c1=c1)




# @app.route('/<float:a>/<oper>/<float:b>/')
# def calculate(a, oper, b):
#     operations = ('+', ':', '**', '-', '*')
#     if oper in operations and oper == '+':
#         res = a+b
#         return render_template('jinja_if2.html', result_cal = res)
#     elif oper in operations and oper == '**':
#         res = a**b
#         return render_template('jinja_if2.html', result_cal = res)
#     elif oper in operations and oper == '-':
#         res = a-b
#         return render_template('jinja_if2.html', result_cal = res)
#     elif oper in operations and oper == '*':
#         res = a*b
#         return render_template('jinja_if2.html', result_cal = res)
#     elif oper in operations and oper == ':' and b == 0:
#         res = 'Ошибка'
#         return render_template('jinja_if2.html', result_cal = res)
#     elif oper in operations and oper == ':':
#         res = a/b
#         return render_template('jinja_if2.html', result_cal = res)
#     else:
#         res = 'Ошибка'
#         return render_template('jinja_if2.html', result_cal = res)

# @app.route('/<float:a>/<oper>/<float:b>/')
# def calculate(a, oper, b):
#     operations = ('+', ':', '**', '-', '*')
#     return render_template('jinja_if2.html', a=a, oper=oper, b=b, operations=operations)


if __name__ == '__main__':
    app.run(debug=True)
