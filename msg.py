"""
@Project ：apiflask 
@File    ：msg.py
@Author  ：AiNiSuBing
@Date    ：2022/7/10 15:30 
程序创建
"""
import os
from app import create_app, db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell

app = create_app(os.getenv("FLASK_CONFIG") or "defaults")
mirgate = Migrate(app, db)
manager = Manager(app)


# @app.shell_context_processors
def make_shell_context():
    return dict(app=app, db=db)  # 这里映射的是写好的类，就是将DB类


manager.add_command('Shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
