# Django Study

## Django开发流程

### 创建项目
django-admin startproject test1
### 创建应用
python manage.py startapp booktest
### 添加应用
test1/settings.py中INSTALLED_APPS下添加应用的名称就可以完成安装。
### 开发服务器
  即时预览效果  
python manage.py runserver ip:端口
例：
python manage.py runserver
### 模型设计
- 通过ORM框架能不写sql语句就可以操作数据库
1. 定义模型类
2. 迁移
3. 