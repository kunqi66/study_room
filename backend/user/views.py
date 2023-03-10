from user.init import user_bp
from flask import request,jsonify
from sql_model import sess,User,Recorde,Stu_class,Site
import json


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8');
        return json.JSONEncoder.default(self, obj)




@user_bp.route('/Login',methods=['GET','POST'])
def Login():
    if request.method == 'POST':
        form = request.form
        data = form.to_dict()
        oid = data.get('oid')
        res = sess.query(User).filter(User.oid == oid).all()

        if res:
            print(res[0].name)
            return json.dumps({
                "suc": True,
                "uid": res[0].id,
                "name":res[0].name,
            })
        else:
            return json.dumps({
                "suc":False,
            })


@user_bp.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        form = request.form
        data = form.to_dict()
        name = data.get('name')
        number = data.get("number")
        student_number = data.get("student_number")
        oid = data.get("oid")
        h = User(name=name, number=number,student_number=student_number,oid=oid,illegal_number=0)
        sess.add(h)
        try:
            sess.commit()
            return json.dumps({
                "suc": True,
                "message": "注册成功",
            })
        except:
            sess.rollback()
            return json.dumps({
                "suc":False,
            })

@user_bp.route('/loadInfo',methods=['GET','POST'])
def loadInfo():
    if request.method == 'POST':
        list=[]
        form = request.form
        data = form.to_dict()
        id = data.get("id")
        form = sess.query(User).filter(User.id == id).all()
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
                "user": list[0],
            }, cls=MyEncoder, indent=4)
        else:
            return json.dumps({
                "suc": False,
                "message": "未查询到数据",
            })


@user_bp.route('/broSite',methods=['GET','POST'])
def broSite():
    if request.method == 'POST':
        form = request.form
        data = form.to_dict()
        start = data.get('start')
        end = data.get("end")
        number = data.get("number")
        uid = data.get("uid")
        print(uid)
        user = sess.query(User).filter(User.id == uid).all()
        stu_number = user[0].student_number
        c_number = data.get("c_number")
        h = Recorde(stu_number=stu_number,zw_number=number,start_time=start,end_time="end",class_number=c_number)
        sess.add(h)
        Room = sess.query(Stu_class).filter_by(id=c_number).all()
        Room[0].number = Room[0].number-1
        site = sess.query(Site).filter_by(id=number).all()
        site[0].state = "E"

        try:
            sess.commit()
            return json.dumps({
                "suc": True,
                "message": "注册成功",
            })
        except:
            sess.rollback()
            return json.dumps({
                "suc":False,
            })




