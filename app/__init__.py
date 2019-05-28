'''
import os
from flask import Flask
import socket

app = Flask(__name__)

# a simple page that says hello
@app.route('/')
def hello():
    html = "<h3>Hello World from {hostname}!</h3>"
    return html.format(hostname=socket.gethostname())

'''
from flask import Flask, render_template, flash, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def get_nums():
    print request.remote_addr
    if request.method == 'GET':
        return render_template('input.html')
    else:
        x = request.form['x']
        y = request.form['y']
    return render_template('output.html', result = int(x)+int(y))
