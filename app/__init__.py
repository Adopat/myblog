# __init__文件用来做初始化作用
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
from logging.handlers import SMTPHandler
# RotatingFileHandler类可以切割和清理日志文件，以确保日志文件在应用运行很长时间不会变得太大
from logging.handlers import RotatingFileHandler
import os
from flask_mail import Mail
from flask_bootstrap import Bootstrap
# 实例化Flask
app = Flask(__name__)
# 读取配置文件
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# Flask-Login 初始化
login = LoginManager(app)
# login视图函数用于处理登录认证
login.login_view = 'login'
mail = Mail(app)
bootstrap = Bootstrap(app)
if not app.debug:
    # ...

    if not os.path.exists('logs'):
        os.mkdir('logs')
    # 设置日志名为microblog.log 日志大小10k
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    # logging.Formatter类为日志消息提供自定义格式 asctime 时间戳 levelname 日志记录级别 message 日志信息
    # pathname 日志来源的代码文件 lineno 行号
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    # 设置日志记录类别info DEBUG<INFO<WARNING<ERROR<CRITICAL
    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')
if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)
from app import routes, models,errors
