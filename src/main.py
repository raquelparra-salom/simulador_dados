from flask import Flask
from flask import request, redirect, url_for
from flask import make_response
from flask import redirect
from random import randint, uniform,random
from flask import render_template
from flask import session
import random 



app =  Flask(__name__)


app.config['SECRET_KEY'] = 'SUPER SECRETO'



@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template("sign_up.html")



def realizarSorteo(veces):
    sorteo = []
    for x in range(0, veces):
        sorteo.append(random.randrange(1,7))

    print(sorteo)
    return sorteo

@app.route('/juego', methods=['GET', 'POST'])
def sorteo():
    nombre = request.form['name']
    numero = request.form['number']
    sorteo = realizarSorteo(int(numero))

    print(nombre)
    return render_template("play.html", nombre=nombre, numero=numero, sorteo=sorteo)

if __name__ == '__main__' :
    app.run('0.0.0.0', 5000,debug=True)
