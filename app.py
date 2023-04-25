from flask import (
    abort, Flask, jsonify, redirect, render_template, request,
    session, url_for
)

from os import system

app = Flask(__name__)
app.secret_key = b'REPLACE_ME_x#pi*CO0@^z_beep_beep_boop_boop'


@app.route('/')
def index():
    return redirect(url_for('fortune'))


@app.route('/fortune/')
def fortune():
    system('fortune | cowsay > output.txt')
    output = open('output.txt', 'r').read()
    return '<pre>' + output + '</pre>'


@app.route('/cowsay/<message>/')
def cowsay(message):
    system(f'cowsay {message}> output.txt')
    output = open('output.txt', 'r').read()
    return '<pre>' + output + '</pre>'
