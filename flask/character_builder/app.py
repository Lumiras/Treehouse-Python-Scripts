from flask import (Flask, render_template, redirect,
                   url_for, request, make_response, flash)
import json

from options import DEFAULTS
app = Flask(__name__)
app.secret_key = 'alkdfsafdsdff35q398yggaiughr345908%@#%ghk'

def get_saved_data():
    try:
        data = json.loads(request.cookies.get('character'))
    except TypeError:
        data = {}
    return data

@app.route('/')
def index():
    data=get_saved_data()
    return render_template('index.html', saves=get_saved_data())

@app.route('/builder')
def builder():
    return render_template(
    'builder.html',
    saves = get_saved_data(),
    options = DEFAULTS
    )

@app.route('/save', methods=['POST'])
def save():
    flash("Saved changes!")
    response= make_response(redirect(url_for('builder')))
    data = get_saved_data()
    data.update(dict(request.form.items()))
    response.set_cookie('character', json.dumps(data))
    return response

app.run(debug=True, host='0.0.0.0', port=7999)
