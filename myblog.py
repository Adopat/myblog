# 导入环境变量的文件名
from app import app,db
from app.models import User,Post
# 添加数据库实例和模型来创建一个shell上下文环境
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


