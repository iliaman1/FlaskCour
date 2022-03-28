from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
@app.route('/<float:num>/')
def index(num):
    pi = 3.14
    return render_template('index.html', name='Ilia', title='Home page', pi=pi, r=num)


@app.route('/filters/')
def task():
    numbers = (7, 5, 8, 0, 3)
    val = '1.69'
    return render_template('filters.html', val=val, numbers=numbers)


@app.route('/jinco/')
@app.route('/<float:a>/<oper>/<float:b>/')
def sintask(a, oper, b):
    numbers = {'string': 0, 'f2': 1, '15': 6, 'g3': -8, '19': 19, 'b2c5f': 11, '09': 90}
    my_list = []
    operations = ('+', ':', '**', '-', '*')
    a1, b1, c1 = 1, 2, 3
    email = 'popov@gmail.com'
    message = 'Flask - это прекрасно!'
    title = 'Обучение'
    return render_template('jinja_static_constructions.html', email=email, message=message, title=title, a=a, oper=oper, b=b, operations=operations, a1=a1, b1=b1, c1=c1, my_list = my_list, numbers = numbers)




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
