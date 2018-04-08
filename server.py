from flask import Flask, render_template, request, redirect, flash, session
import re
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    count = 0
    if len(request.form['emailhtml']) < 1:
        flash("Email cannot be empty!")
        return redirect("/")
    elif not EMAIL_REGEX.match(request.form['emailhtml']):
        flash("Invalid Email!")
        return redirect("/")
    else:
        email = request.form['emailhtml']
        count+=1

    if not NAME_REGEX.match(request.form['fnamehtml']) or not NAME_REGEX.match(request.form['lnamehtml']):
        flash("Invalid name!")
        return redirect("/")
    else:
        fname = request.form['fnamehtml']
        lname = request.form['lnamehtml']
        count+=1
        
    if len(request.form['passwordhtml']) < 1 or len(request.form['passwordhtml']) <= 8:
        flash("Password cannot be empty or needs to be at least 8 characters long!")
        return redirect("/")
    else:
        if request.form['passwordhtml'] != request.form['password2html']:
            flash("Passwords need to match!")
            return redirect("/")
        elif request.form['passwordhtml'] == request.form['password2html']:  
            count+=1
            password = request.form['passwordhtml']
            password2 = request.form['password2html']

    
    if count == 3:
        return render_template('result.html',fnamehtml = fname, lnamehtml = lname, emailhtml = email, passwordhtml = password, password2html = password2)



app.run(debug=True) # run our server