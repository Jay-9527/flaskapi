"""
@Project ：apiflask 
@File    ：index.py
@Author  ：AiNiSuBing
@Date    ：2022/7/10 13:13 
"""
from flask import Blueprint

# users API

bp = Blueprint("index", __name__, url_prefix="/")


@bp.route("/")
def login():
    return "首页 API"
