"""
-*- coding:utf-8 -*-
@File: backend.py
@Author: kkhan
@DateTime: 2023/7/25 22:03
@Description:
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World TD!'


if __name__ == '__main__':
    app.run()
