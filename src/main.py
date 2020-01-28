from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import render_template



app =  Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    
    return render_template('index.html')
   


if __name__ == '__main__' :
    app.run('0.0.0.0', 5000,debug=True)
