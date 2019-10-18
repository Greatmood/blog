# 应用程序包

from flask import Flask
from config import config
from blopApp.main import blog_blue


# 创建app对象
def create_app():
    app = Flask(__name__)
    app.register_blueprint(blog_blue)
    app.config.from_object(config["development"])
    from blopApp.ext import init_ext
    init_ext(app)

    return app