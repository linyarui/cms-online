#coding:utf-8

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from apps import create_app
from exts import db
# 导入模型
from apps.cms import models


# 执行命令
# python manage.py db init:初始化
# python manage.py db migrate:执行迁移脚本
# 有可能报AttributeError: 'NoneType' object has no attribute 'encoding'的错误,是因为写数据库连接的时候,utf8写成了utf-8
# python manage.py db upgrade:映射到数据库中

app = create_app()

# 初始化app
manager = Manager(app)

# 绑定
Migrate(app, db)
# 映射
manager.add_command('db', MigrateCommand)


# 添加cms用户
@manager.option('-u', '--username', dest='username')
@manager.option('-p', '--password', dest='password')
@manager.option('-e', '--email', dest='email')
def create_cms_user(username, password, email):
    user = models.CMSUser(username=username, password=password, email=email)
    db.session.add(user)
    db.session.commit()
    print("cms用户添加成功")
# 添加数据
# python manage.py create_cms_user -u admin -p 123456 -e admin@admin.com


if __name__ == '__main__':
    manager.run()



