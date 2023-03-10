from settings import MYSQL_URL

from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker  # 创建连接
from sqlalchemy.ext.declarative import declarative_base  # 创建表的基类

engine = create_engine(
    # //用户名:密码@IP地址:端口/数据库
    MYSQL_URL,
    pool_size=10,  # 连接池大小
    # 超过连接池大小外最多可以创建的连接，也就是一共可以创建15个连接
    max_overflow=5,
    echo=True,  # 调试信息展示
)

Session = sessionmaker(bind=engine)
sess = Session()  # 创建连接  在其他文件使用import导入

Base = declarative_base()


class Host(Base):
    __tablename__ = 'hosts_test'  # 表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(64), unique=True, nullable=False)
    ip_addr = Column(String(126), unique=True, nullable=False)
    port = Column(Integer, default=8080)


class User(Base):
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    oid = Column(String(200),unique=True,nullable=False)
    name = Column(String(24),nullable=False)
    student_number = Column(String(24),unique=True,nullable=False)
    number = Column(String(14),unique=True,nullable=False)
    illegal_number=Column(Integer)

class Manager(Base):
    __tablename__ = 'manager'  # 表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), unique=True, nullable=False)
# 座位号，日期，原因

class Complaint(Base):
    __tablename__ = 'Complaint'  # 表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    class_number = Column(String(20))
    number = Column(String(20),nullable=False)
    date = Column(String(10), nullable=False)
    reason = Column(String(60),nullable=False)
    result = Column(String(1))


class Recorde(Base):
    __tablename__ = 'Recorde'  # 表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    stu_number = Column(String(50),nullable=False)
    class_number = Column(Integer)
    zw_number = Column(Integer)
    start_time = Column(String(20))
    end_time = Column(String(20))

class Notice(Base):
    __tablename__ = 'Notice'  # 表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(20),nullable=False)
    text = Column(String(200),nullable=False)
    date = Column(String(20),nullable=False)

class Stu_class(Base):
    __tablename__ = 'Stu_class'  # 表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(10),nullable=False)
    number = Column(Integer,nullable=False)

class Site(Base):
    __tablename__ = 'Site'  # 表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    state = Column(String(1), nullable=True)   # 可用A，不可用E



if __name__ == '__main__':
    Base.metadata.create_all(engine)  # 创建表
    """
    h1 = Notice(title='公告1', text="好好学习，卷起来",date="2023.04.01")
    h2 = Notice(title='公告2',
                text="图书馆自习室是供图书馆所有持证读者学习的场所。每位读者都拥有使用自习座位的权利，同时还应该履行维护公共秩序和保持环境卫生的义务。",
                date="2023.04.01")
    h3 = Notice(title='公告3', text="我看谁在卷", date="2023.04.01")
    h4 = Notice(title='公告4',
                text="公告功能测试",
                date="2023.04.01")
    sess.add(h1)
    sess.add(h2)
    sess.add(h3)
    sess.add(h4)
    sess.commit()
"""
    # 主管理员创建信息
    """
    manager_main = Manager(email="2839078819@qq.com", password="my123")
    sess.add(manager_main)
    sess.commit()
    """
    """
    i = 0
    while i < 60:
        h = Site(state='A')
        sess.add(h)
        sess.commit()
        i = i+1
    """
    """
    h1 = Stu_class(title='一号自习室',number=20)
    h2 = Stu_class(title='二号自习室', number=20)
    h3 = Stu_class(title='三号自习室', number=20)
    h4 = Stu_class(title='四号自习室', number=20)
    h5 = Stu_class(title='五号自习室', number=20)
    h6 = Stu_class(title='六号自习室', number=20)
    sess.add(h1)
    sess.add(h2)
    sess.add(h3)
    sess.add(h4)
    sess.add(h5)
    sess.add(h6)
    sess.commit()
    # 操作数据库过程示例
    """
    """

    Session = sessionmaker(bind=engine)
    sess = Session()  # 创建连接
    # 添加数据
    h = Host(hostname='test1', ip_addr='127.0.0.1')
    h2 = Host(hostname='test2', ip_addr='192.168.1.1', port=8080)
    h3 = Host(hostname='test3', ip_addr='192.168.1.2', port=8081)

    # 添加数据
    sess.add(h)  # 添加一条数据
    sess.add_all([h2, h3])  # 添加多条数据

    # 删除数据
    sess.query(Host).filter(Host.id > 1).delete()

    # 更新数据
    sess.query(Host).filter(Host.id == 1).update({'port': 3309})

    # 查询数据
    # res=sess.query(Host).filter(Host.id==1).all()
    # 查询数据的第二种写法
    res = sess.query(Host).filter_by(id=1).all()
    for r in res:
        print(r.hostname, r.port)

    sess.commit()  # 提交
    """
