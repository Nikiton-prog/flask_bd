from flask import Flask, render_template, redirect
from loginform import LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)

@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)

@app.route('/list_prof/<marker>')
def list_prof(marker):
    with open("static/resource/prof.txt", encoding='utf-8') as f:
        data = f.readlines()
    return render_template('list_prof.html', marker=marker, data=data)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    data = {}
    data['title'] = 'Анкета'
    data['Фамилия'] = 'Wanty'
    data['Имя'] = 'Mark'
    data['education'] = 'выше среднего'
    data['profession'] = 'штурман'
    data['sex'] = 'male'
    data['motivation'] = 'Всегда мечтал!'
    data['ready'] = True
    return render_template('auto_answer.html', data=data)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print(form.username)
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/success')
def success():
    return render_template('base.html', title="Успешно")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')