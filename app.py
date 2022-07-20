"""
这里是创建程序和实例化程序
"""
import os

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from Config import configs
from modelu import Users_bp
from modelu import Index_bp

# defined one cut
# class user1:
#     {'type', '1', 'name', 'password', 'status', {'massge': '200'}}
# app = APIFlask(__name__, docs_ui='redoc')

# 定义数据库
db = SQLAlchemy()


def create_app(path=None):
    if path is None:
        path = os.getenv("FLASK_CONFIG", "defaults")
    app = Flask(__name__)
    app.config.from_object(configs[path])
    configs[path].init_app(app)
    # 注册蓝图
    app.register_blueprint(Users_bp)
    app.register_blueprint(Index_bp)
    return app


# 初始化好项目
# app = Flask(__name__)
# app.config.from_object(config[config])
# db.init_app(app)  # 这里是将db绑定到项目中



