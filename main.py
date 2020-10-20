from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from app import app, db
from app.models import User

db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        pwd = request.form['password']
        if name and email and pwd:    
            user = User(name, email, pwd)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']

        if User.query.filter_by(email=email).first():
            """Verifica se o usuário existe"""
            if User.query.filter_by(email=email).first().verify_password(pwd):
                """Verifica se a senha está correta"""
                login_user(User.query.filter_by(email=email).first())
                return redirect(url_for('home'))
        else:
            return redirect(url_for('register'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


app.run(debug=True)