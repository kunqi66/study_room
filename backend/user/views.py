from user.init import user_bp
from flask import request,jsonify

import json


from user.init import user_bp
from flask import request,jsonify
from sql_model import sess,User,Video,News
import json


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8');
        return json.JSONEncoder.default(self, obj)


@user_bp.route('/')
def get_goods():
    return "get user"




@user_bp.route('/Login',methods=['GET','POST'])
def Login():
    if request.method == 'POST':
        form = request.form
        data = form.to_dict()
        oid = data.get('oid')
        res = sess.query(User).filter(User.wx_token == oid).all()
        if res:
            return json.dumps({
                "suc": True,
                "uid": res[0].id,
            })
        else:
            return json.dumps({
                "suc":False,
                "uid":res[0].id,
            })


