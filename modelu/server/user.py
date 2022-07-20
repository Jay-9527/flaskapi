"""
@Project ：apiflask 
@File    ：user.py
@Author  ：AiNiSuBing
@Date    ：2022/7/10 13:06 
用户界面 API [ 蓝图方式管理 ]
"""
from flask import Blueprint

# users API

bp = Blueprint("users", __name__, url_prefix="/user")


@bp.route("/login")
def login():
    return "用户API"
