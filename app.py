#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, send_from_directory, make_response
import subprocess, os
import urllib.parse

DEVELOPMENT_ENV  = True

app = Flask(__name__)

app_data = {
    "name":         "Start Here",
    "description":  "A basic Flask app using bootstrap for layout",
    "author":       "Cooper Wallace",
    "html_title":   "Cooper's Gymnasium Adventure",
    "project_name": "cmdLineLern",
    "keywords":     "flask, webapp, template, basic"
}


@app.route('/')
def index():
    return render_template('index.html', app_data=app_data)


@app.route('/pwd', methods= ['GET'])
def pwd():
    return os.getcwd()

@app.route('/user_input', methods = ['GET','POST'])
def user_input():
    v = request.args.get('user_input_field')
    cmdDecode = urllib.parse.unquote(v)

    if "cd" in cmdDecode:
        cmdDecode = cmdDecode.split()
        newDir = cmdDecode[1]
        print("Uinput: cd "+newDir)
        os.chdir(cmdDecode[1])
        print(os.listdir(os.getcwd()))
        return os.getcwd()

    try:
        cmdDecode = cmdDecode.split()
    except:
        print('end')

    cmd = cmdDecode
    print(cmd)
    p = subprocess.Popen(cmd, stdout= subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()
    return out


@app.route('/about')
def about():
    return render_template('about.html', app_data=app_data)


@app.route('/service')
def service():
    return render_template('service.html', app_data=app_data)


@app.route('/start')
def contact():
    return render_template('start.html', app_data=app_data)

@app.route('/grep-landing')
def greplanding():
    return render_template('grep/grep-landing.html', app_data=app_data)

@app.route('/js/<path:path>')
def send_img(path):
    return send_from_directory('js', path)

if __name__ == '__main__':
    app.run(debug=DEVELOPMENT_ENV)