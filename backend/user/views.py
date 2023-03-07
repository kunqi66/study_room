from user.init import user_bp
from flask import request,jsonify
from sql_model import sess,User
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
        h = User(name=name, number=number,student_number=student_number,oid=oid)
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





