import hashlib
from datetime import datetime
import os
from manager.init import manager_bp
from flask import request,jsonify
from sql_model import sess,Manager,Stu_class,Notice,Site,Complaint,User,Recorde
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


@manager_bp.route('/loadRecord',methods=['GET','POST'])
def loadRecord():
    if request.method == 'POST':
        list = []
        form = sess.query(Recorde).all()
        for r in form:
            list.append({
                "start": r.start_time,
                "end":r.end_time,
                "class_number": r.class_number,
                "site_number": r.zw_number,
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




@manager_bp.route('/SYGG',methods=['GET','POST'])
def SYGG():
    if request.method == "POST":
        form = request.form
        data = form.to_dict()
        id = data.get("editid")
        print(id)
        res =sess.query(Notice).filter(Notice.id == id).all()
        if res:
            res[0].title = data.get("title")
            res[0].text = data.get("text")
            res[0].date = data.get("date")
            sess.commit()
            return json.dumps({
                "suc": True,
                "message": "修改成功",
            })
        else:
            return json.dumps({
                "suc": False,
                "message": "未查询到数据",
            })



@manager_bp.route('/submitNotice',methods=['GET','POST'])
def submitNotice():
    if request.method == 'POST':
        print("执行")
        form = request.form
        data = form.to_dict()
        title = data.get("title")
        text = data.get("text")
        print("提取")
        date = data.get("date")
        message = Notice(title=title,text=text,date=date)
        sess.add(message)
        try:
            sess.commit()
            print("保存成功")
            return json.dumps({
                "suc": True,
                "message": "上传成功",
            })
        except:
            sess.rollback()
            return json.dumps({
                "suc":False,
                "message":"上传失败",
            })






@manager_bp.route('/loadComp',methods=['GET','POST'])
def loadComp():
    if request.method == 'POST':
        list = []
        form = sess.query(Complaint).all()
        for r in form:
            list.append({
                "class_number": r.class_number,
                "number": r.number,
                "date": r.date,
                "reason": r.reason,
                "result": r.result,
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

@manager_bp.route('/dealComp',methods=['GET','POST'])
def dealComp():
    if request.method == "POST":
        form = request.form
        data = form.to_dict()
        id = data.get("id")
        res =sess.query(Complaint).filter(Complaint.id == id).all()
        if res:
            res[0].result = data.get("result")
            sess.commit()
            return json.dumps({
                "suc": True,
                "message": "修改成功",
            })
        else:
            return json.dumps({
                "suc": False,
                "message": "未查询到数据",
            })


@manager_bp.route('/loadUser',methods=['GET','POST'])
def loadUser():
    if request.method == 'POST':
        list = []
        form = sess.query(User).all()
        for r in form:
            list.append({
                "name": r.name,
                "student_number": r.student_number,
                "number": r.number,
                "illegal_number": r.illegal_number,
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


@manager_bp.route('/dealSite',methods=['GET','POST'])
def dealSite():
    if request.method == "POST":
        form = request.form
        data = form.to_dict()
        id = data.get("id")
        c_number = data.get("c_id")
        print(c_number)
        Room = sess.query(Stu_class).filter_by(id=c_number).all()
        Room[0].number = Room[0].number - 1
        res = sess.query(Site).filter(Site.id == id).all()
        if res:
            res[0].state = data.get("result")
            sess.commit()
            return json.dumps({
                "suc": True,
                "message": "修改成功",
            })
        else:
            return json.dumps({
                "suc": False,
                "message": "未查询到数据",
            })




@manager_bp.route('/submitComp',methods=['GET','POST'])
def submitComp():
    if request.method == 'POST':
        print("执行")
        form = request.form
        data = form.to_dict()
        room = data.get("room")
        site = data.get("site")
        reason = data.get("reason")
        time = data.get("time")
        message = Complaint(class_number=room,number=site,date=time,reason=reason,result='W')
        sess.add(message)
        sess.commit()
        print("保存成功")
        return json.dumps({
            "suc": True,
            "message": "上传成功",
        })


