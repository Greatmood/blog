# 视图函数

from flask import Blueprint


blog_blue = Blueprint("blog_blue", __name__)


@blog_blue.route("/")
@blog_blue.route("/index")
def index():
    return "Start Blog"

