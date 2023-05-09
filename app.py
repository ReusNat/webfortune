from flask import (
    abort, Flask, jsonify, redirect, render_template, request,
    session, url_for
)

from os import system
import subprocess

app = Flask(__name__)
app.secret_key = b'REPLACE_ME_x#pi*CO0@^z_beep_beep_boop_boop'


@app.route('/')
def index():
    return redirect(url_for('fortune'))


@app.route('/fortune/')
def fortune():
    output = subprocess.check_output('fortune',
                                     shell=True).decode()
    return '<pre>' + output + '</pre>'


@app.route('/cowfortune/')
def cowfortune():
    output = subprocess.check_output('fortune | cowsay',
                                     shell=True).decode()
    return '<pre>' + output + '</pre>'


@app.route('/cowsay/<message>/')
def cowsay(message):
    output = subprocess.check_output('cowsay %s' %message,
                                     shell=True).decode()
    return '<pre>' + output + '</pre>'
