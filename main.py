from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/index_old/')
@app.route('/<float:num>/')
def index_old(num):
    pi = 3.14
    return render_template('index_old.html', name='Ilia', title='Home page', pi=pi, r=num)


@app.route('/filters/')
def task():
    numbers = (7, 5, 8, 0, 3)
    val = '1.69'
    return render_template('filters.html', val=val, numbers=numbers)


@app.route('/test/')
def test():
    return render_template('test.html', )


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
    varargs = [1, 10, 100, 1000, 10000, ]
    kwargs = {'11111': 'm', '10': 'o', '1': 'r', '111': 'i', '666': 'e', }
    return render_template('jinja_static_constructions.html', varargs=varargs, kwargs=kwargs, email=email,
                           message=message, title=title, a=a, oper=oper, b=b, operations=operations, a1=a1, b1=b1,
                           c1=c1, my_list=my_list, numbers=numbers)


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
