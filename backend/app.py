from flask import Flask
from user.init import user_bp
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'
app.register_blueprint(user_bp,url_prefix="/user")

if __name__ == '__main__':
    app.run()
