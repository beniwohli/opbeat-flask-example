# -*- coding: utf-8 -*-

import os

from flask import Flask, render_template, request, redirect, url_for
from opbeat.contrib.flask import Opbeat

app = Flask(__name__)
opbeat = Opbeat(app)


@app.route('/')
def index():
    return 'OK'


@app.route('/error')
def error():
    raise ValueError(request.args.get('error', ''))


if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port)
