from flask import Flask, render_template, request, redirect, url_for, make_response, session
from flask import current_app as app
from .models import User, Shops
from .database import db
from flask_mail import Mail, Message
import secrets 
import random
from app1 import mail

@app.route("/search", methods=["POST"])
def search():
    if request.method == 'POST':
        option = request.form.get("options")
        lca = request.form['LCA']
        if request.form["clicked"] == "Search":
            print(option, lca)
            
            if option == "Shops":
                
                data = Shops.query.filter_by(slocality = lca.lower()).all()
            
            x = []
            for i in range(len(data)):
                x.append((data[i].sname, data[i].slocality, data[i].sdescription,
                data[i].saddress, data[i].notc, data[i].imgloc, data[i].scontact))

            print(data)
            return render_template('aftersearch.html', count=len(data), data=x)