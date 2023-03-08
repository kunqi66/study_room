import hashlib
from datetime import datetime
import os
from manager.init import manager_bp
from flask import request,jsonify
from sql_model import sess,Manager,Stu_class,Notice,Site
import json

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8');
        return json.JSONEncoder.default(self, obj)


@manager_bp.route('/Login',methods=['GET','POST'])
def Login():
    if request.method == 'POST':
        form = request.form
        data = form.to_dict()
        res = sess.query(Manager).filter(Manager.email == data.get("account")).all()
        if res:
            if res[0].password == data.get("password"):
                return json.dumps({
                    "suc": True,
                    "message": "登录成功",
                })
            else:
                return json.dumps({
                    "suc": False,
                    "message": "密码错误",
                })
        else:
            print("未查询到数据")
            return json.dumps({
                "suc": False,
                "message": "邮箱未被赋予管理员权限",
            })


@manager_bp.route('/loadRoom',methods=['GET','POST'])
def loadRoom():
    if request.method == 'POST':
        list = []
        form = sess.query(Stu_class).all()
        for r in form:
            list.append({
                "title": r.title,
                "number": r.number,
            })
        if form:
            return json.dumps({
                "suc": True,
                "form": list,
            }, cls=MyEncoder, indent=4)
        else:
            return json.dumps({
                "suc": False,
                "message": "未查询到数据",
            })


@manager_bp.route('/loadNotice',methods=['GET','POST'])
def loadNotice():
    if request.method == 'POST':
        list = []
        form = sess.query(Notice).all()
        for r in form:
            list.append({
                "notice_title": r.title,
                "notice_text": r.text,
                "notice_time":r.date,
            })
        if form:
            return json.dumps({
                "suc": True,
                "form": list,
            }, cls=MyEncoder, indent=4)
        else:
            return json.dumps({
                "suc": False,
                "message": "未查询到数据",
            })


@manager_bp.route('/loadSite',methods=['GET','POST'])
def loadSite():
    if request.method == 'POST':
        list = []
        form = sess.query(Site).all()
        for r in form:
            list.append({
                "id": r.id,
                "status": r.state,
            })
        if form:
            return json.dumps({
                "suc": True,
                "form": list,
            }, cls=MyEncoder, indent=4)
        else:
            return json.dumps({
                "suc": False,
                "message": "未查询到数据",
            })