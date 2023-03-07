from flask import Flask
from user.init import user_bp
from manager.init import manager_bp

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


app.register_blueprint(user_bp, url_prefix="/user")

app.register_blueprint(manager_bp, url_prefix="/manager")

if __name__ == '__main__':
    app.run()
