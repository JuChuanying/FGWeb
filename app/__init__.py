'''
初始化 Flask 应用
'''

from flask import Flask

def create_app():
    app = Flask(__name__,static_folder='/home/d/jcy/Web/FGWeb/app/static')
    from .views import main
    app.register_blueprint(main)
    return app
