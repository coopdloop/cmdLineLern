#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template

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


if __name__ == '__main__':
    app.run(debug=DEVELOPMENT_ENV)