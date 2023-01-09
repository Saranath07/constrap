from flask import Flask, render_template, request, redirect, url_for, make_response, session
from flask import current_app as app
from .models import User, Shops
from .database import db
from flask_mail import Mail, Message
import secrets 
import random
from app1 import mail


@app.route('/')
def home():
    return render_template('index.html', state="Login / Register")


@app.route('/regstration1')
def registration1():
    return render_template('registration1.html')


@app.route('/otp', methods=['POST'])
def otp():
    if request.method == 'POST':
        otp = request.form['OTP']
        if request.form['clicked'] == "Register":
            if otp == computer_genereted_otp:
                sql = User(username = d[1], password = d[3], email = d[2], name = d[0], phone_number = d[-1])
                db.session.add(sql)
                db.session.commit()

    return render_template("index.html", state="Login / Register")


@app.route('/authentication', methods=['POST'])
def authentication():
    if request.method == 'POST':
        name = request.form['Name']
        username = request.form['Username']
        email = request.form['Email']
        pno = request.form['PNo']
        password = request.form['Password']
        cpassword = request.form['CPassword']
        global d
        d = (name, username, email, password, str(pno))
        if request.form['clicked'] == "Send OTP":
            d = (name, username, email, password, str(pno))
            msg = Message(
                subject='OTP', sender="constapTS@gmail.com", recipients=[email])
            global computer_genereted_otp
            computer_genereted_otp = str(random.randint(1000, 9999))
            msg.body = "Your OTP is " + computer_genereted_otp
            mail.send(msg)

    print(name, username, email, pno, password, cpassword)
    return "", 204


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        sql = db.session.query(User).filter((User.email == email) & (User.password == password)).first()
        if sql:
            return render_template('index.html', state="Logout")
        return render_template("none.html")
    if request.form['clicked'] == 'Register':
        return render_template('registration.html')


@app.route('/logout', methods=['POST'])
def logout():
    if request.form['clicked'] == "LOGOUT":
        return render_template('index.html', state="Login / Register")


@app.route('/register', methods=['POST'])
def register():
    if request.form['clicked'] == "Forgot Password":
        return render_template('none.html')
    elif request.form['clicked'] == "Register":
        return render_template('registration.html')
