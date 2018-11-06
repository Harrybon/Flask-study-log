import os

# 参数部分
options={
    'port':8000,
}

# 配置
BASE_DIRS = os.path.dirname(__file__)
settings={
    'debug':True,
    'static_path':os.path.join(BASE_DIRS,'static'),
    'template_path':os.path.join(BASE_DIRS,'templates')
}