from flask import (
    abort, Flask, jsonify, redirect, render_template, request,
    session, url_for
)

app = Flask(__name__)
app.secret_key = b'REPLACE_ME_x#pi*CO0@^z_beep_beep_boop_boop'


@app.route('/')
def index():
    return 'Results of GET /'
