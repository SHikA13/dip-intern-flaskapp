from flask import Flask,request,render_template,Response
from flask.helpers import make_response
import numpy as np
import pandas as pd
import pickle
from fix import data_fix
from fix import column
import flask
import learn


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('flask_api_index.html')

@app.route('/upload',methods=['POST'])
def upload():
    if 'file' not in flask.request.files:
        return 'ファイル未指定'

    fs = flask.request.files['file']

    app.logger.info('file_name={}'.format(fs.filename))
    app.logger.info('content_type={} ,content_length={}, mimetype={},mimetype_params={}'.format(
        fs.content_type, fs.content_length, fs.mimetype, fs.mimetype_params))

    fs.save('test_x.csv')

    return render_template('upload.html')


@app.route('/result')
def result():    
    return render_template('result.html')

@app.route('/download/')
def download():

    data = learn.machine_learn()

    response = make_response()
    response.data = data.getvalue().encode("utf-8-sig")
    response.headers['Content-Disposition'] = 'attachment; filename=file.csv'
    response.headers['Content-type']='text/csv'

    return response

if __name__ == '__main__':
    app.run(debug = True)