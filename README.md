# django-orm-only
###### 个人主页：[JeffyLu's Personal Page](https://jeffylu.github.io/)
- - -

参考了一下网上其他单独使用django orm的方案, 感觉都太麻烦了, 整合一下个人感觉自己的版本最简单, 看一下项目结构:

		django-orm-only/
		├── db
		│   ├── __init__.py
		│   ├── migrations
		│   │   └── __init__.py
		│   └── models.py
		├── manage.py
		└── test.py

### 简单说明
- ```db```文件夹里的```migrations```放的是每次数据表迁移文件.
- ```models.py```定义数据表.
- ```manage.py```主要的配置都在这里面.
- ```test.py```脚本.

### 测试

##### 迁移数据库
```
$ python3 manage.py makemigrations

	Migrations for 'db':
	  db/migrations/0001_initial.py:
	    - Create model TestDb

$ python3 manage.py migrate

	Operations to perform:
	  Apply all migrations: db
	Running migrations:
	  Rendering model states... DONE
	  Applying db.0001_initial... OK
```

##### 测试脚本
```
$ python3 test.py

	TestDb object
```