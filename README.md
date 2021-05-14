## 第一章：Hello world

### 1.1 安装Python

### 1.2 安装Flask

### 1.3 虚拟环境配置

```python
# 命令如下
mkdir myblog
cd myblog
# 运行venv 包，创建一个名为venv的虚拟环境
python3 -m venv venv
# 激活虚拟环境
source venv/bin/activate
# 在虚拟环境安装Flask
pip install Flask
```

> 强烈建议使用Pycharm 不用配置这么麻烦，直接新建项目的时候选择虚拟环境就可以

### 1.4配置自动生效的环境变量

```python
# 1.安装python-dotenv
pip install python-dotenv
# 2.创建.flaskenv
FLASK_APP=myblog.py
# 3.运行项目
Flask run
```

## 第二章 模板

将实现程序的后台逻辑和网页布局划分开来。模板保存在在templates文件夹中。

```python
mkdir app/templates
```

将模板转换为HTML页面的操作称为渲染，为了渲染模板，需要从Flask框架中导入render_template()函数，render_template()函数调用Flask原生依赖Jinja2模板引擎。

模板的继承

## 第三章 web表单

- FLASK-WTF 插件用来处理web表单

- 配置密钥,为后续表单字段加密

  ```python
  # config.py
  import os
  
  class Config(object):
      SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
  ```

  

- 读取配置文件 在`__init__`文件中

  ```python
  from flask import Flask
  from cofig import Config
  app = Flask(__name__)
  app.config.from_object(Config)
  from app import routes
  ```

## 第四章 数据库

### 4.1 安装ORM

```python
pip install flask-sqlalchemy
```

### 4.2 数据库迁移

```python
# 1.数据库初始化,生成migrations 目录
flask db init  
# 2.生成迁移脚本
flask db migrate -m 'user table'
# 3.更改应用配置
flask db upgrade
```

> 一旦变更了数据库模型，就要生成一个新的数据库迁移1.flask db migrate 2.flask db upgrade

### 4.3 Flask-SQLALchemy配置

```python
# config.py
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

### 4.4 插件注册

```python
# __init__.py
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
```

> 数据库在应用的表现形式上是一个数据库实力，我们需要在应用实例化后进行实例化的注册的操作，在`__init__.py`

### 4.5 数据库操作

```python
# 1.增加用户
u = User(username='Susan',email='Susan@example.com')
db.session.add(u)
db.session.commit()
# 2.全部查询
users = User.query.all()
users
for u in users:
    print(u.id,u.username)
# 3.单一查询
u = User.query.get(1)
u

```

### 4.6 Shell上下文

```python
'''
app.shell_context_processor装饰器将该函数注册为一个shell上下文函数。 当flask shell命令运行时，它会调用这个函数并在shell会话中注册它返回的项目。 函数返回一个字典而不是一个列表，原因是对于每个项目，你必须通过字典的键提供一个名称以便在shell中被调用。
在添加shell上下文处理器函数后，你无需导入就可以使用数据库实例：
'''
from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
```

## 第五章 用户登录

### 5.1 密码哈希

### 5.2 Flask-Login插件

该插件管理用户登录状态，以便用户可以登录到应用，然后在用户导航到该应用的其他页面时，应用会记得该用户已经登录。

## 第六章 个人主页和头像

## 第七章 错误处理
