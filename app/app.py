#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, send_from_directory, make_response
import subprocess, os, sys
from subprocess import check_output
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
    BI = ('BAD INPUT, try again!')


    if "cd" in cmdDecode:
        try:
            cmdDecode = cmdDecode.split()
            newDir = cmdDecode[1]
            print("Uinput: cd "+newDir)
            os.chdir(cmdDecode[1])
            print(os.listdir(os.getcwd()))
            return os.getcwd()
        except:
            return BI

    try:
        cmdDecode = cmdDecode.split()
        cmd = cmdDecode
        print(cmd)

        p = check_output(cmd)
        #p = subprocess.Popen(cmd, stdout= subprocess.PIPE,
        #                    stderr=subprocess.PIPE,
        #                    stdin=subprocess.PIPE)
        #out,err = p.communicate()
        return p
    except Exception as e:
        return str(e)
    

@app.route('/about')
def about():
    return render_template('about.html', app_data=app_data)


@app.route('/service')
def service():
    return render_template('service.html', app_data=app_data)


@app.route('/start', methods=['GET','POST'])
def contact():
    data = {
        'Subject01': 'Challenge Subject 01',
        'Subject02': 'Challenge Subject 02',
        'Subject03':'Challenge Subject 03',
        'Subject04':'Challenge Subject 04'
    }
    return render_template('start.html', app_data=app_data,chal=data)

@app.route('/grep-landing')
def grep():
    data = {
        'Question_01_help': 'Grep Challenge 01',
        'Question_01': 'This is the question!',
        'Question_01_hint':'hint_here'
    }
    return render_template('landing.html', app_data=app_data,ctf_data=data)


@app.route('/sed-landing')
def sed():
    data = {
        'Question_01_help': 'Sed Challenge 01',
        'Question_01': 'This is the question!',
        'Question_01_hint':'hint_here'
    }
    return render_template('landing.html', app_data=app_data,ctf_data=data)

@app.route('/awk-landing')
def awk():
    data = {
        'Question_01_help': 'Awk Challenge 01',
        'Question_01': 'This is the question!',
        'Question_01_hint':'hint_here'
    }
    return render_template('landing.html', app_data=app_data,ctf_data=data)

@app.route('/uniq-landing')
def uniq():
    data = {
        'Question_01_help': 'Uniq Challenge 01',
        'Question_01': 'This is the question!',
        'Question_01_hint':'hint_here'
    }
    return render_template('landing.html', app_data=app_data,ctf_data=data)

@app.route('/js/<path:path>')
def send_img(path):
    return send_from_directory('js', path)

if __name__ == '__main__':
    app.run(debug=DEVELOPMENT_ENV, host='0.0.0.0')