import os
# 数据库配置
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://kunqi:Kunqi666@rm-2ze20n03b453k99877o.mysql.rds.aliyuncs.com:3306/study_room'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# 项目相关全局变量配置
MYSQL_URL = 'mysql+pymysql://kunqi:Kunqi666@rm-2ze20n03b453k99877o.mysql.rds.aliyuncs.com:3306/study_room'
TOKEN_DIC = {}

UID = []
# 获取当前文件的目录
cur_path = os.path.abspath(os.path.dirname(__file__))
