"""
-*- coding:utf-8 -*-
@File: backend.py
@Author: kkhan
@DateTime: 2023/7/25 22:03
@Description:
"""
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World Love Yesterday!'

# 首页
class Main(Resource):
    def get(self):
        return {'hello': 'world'}


# 用户管理
class UserApi(Resource):
    def get(self):
        return {'hello': 'world'}


# 测试用例管理
class TestCaseApi(Resource):
    def get(self):
        return {'hello': '测试用例'}


# 任务管理
class TaskApi(Resource):
    def get(self):
        return {'hello': '任务管理'}


# 报告管理
class ReportApi(Resource):
    def get(self):
        return {'hello': '报告管理'}


api.add_resource(Main, '/')
api.add_resource(UserApi, '/login')
api.add_resource(TestCaseApi, '/testcase')
api.add_resource(TaskApi, '/task')
api.add_resource(ReportApi, '/report')

if __name__ == '__main__':
    app.run(debug=True)
