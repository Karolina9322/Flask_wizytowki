from flask import Flask

from flask import request, redirect

from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Dzień dobry! Zapraszam na moją stronę domową."

@app.route('/mypage/me')
def mypage_me():
    return render_template("Moja_strona_1.html")


@app.route("/mypage/contact", methods=['GET', 'POST'])
def mypage_contact():
    if request.method == 'GET':
        print("We received GET")
        return render_template("Moja_strona_2.html")
    elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       
    

