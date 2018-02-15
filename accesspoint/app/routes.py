from app import app, db
from flask import render_template, redirect, url_for, request
from app.forms import LoginForm, RegisterForm
from app.models import Idiot

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
            return redirect(url_for('success'))
    return render_template('index.html', form=form, title="B-Sides Canberra Offical WiFi 2018")

@app.route('/success')
def success():
    return "Success"

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        agent = "OS: " + request.user_agent.platform + " / Browser: " + request.user_agent.browser
        user = Idiot(username=form.username.data, password=form.password.data, user_agent=agent)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('fools'))
    
    return render_template('register.html', form=form, title="Register for Account")

@app.route('/fools')
def fools():
    return "You are a fool"

@app.route('/wall')
def wall():
    idiots = Idiot.query.all()

    return render_template('wall.html', idiots=idiots, title="Wall of Idiots")

@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for(index))

@app.errorhandler(400)
def bad_request(e):
    return redirect(url_for(index))

