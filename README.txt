以下为部署文档   日常使用时  直接去使用 使用文档


使用 flask 框架   cookiecutter https://github.com/sloria/cookiecutter-flask.git
 克隆 项目
 git clone git@github.com:13923858795/new_quatek.git
 cd new_quatek

部署流程

1：  安装 python3.6
2：  安装pip, pipenv, 安装 mysql 服务器


4:   进入项目根目录   /root/new_quatek
     执行pipenv shell  进入 虚拟环境   (  一键导出当前依赖   pip freeze > requirement.txt  )

5:   执行  pip install -r requirements.txt

6:   自动创建数据库模型 （如数据库通过其他方式创建，此步跳过）
            flask db init
            flask db migrate
            flask db upgrade


7: 启动 web 服务：
   默认端口 5000 启动方式：
            flask run
   指定端口启动：
            flask run -h 0.0.0.0 -p 8080
   gunicorn 启动：
            gunicorn myflaskapp.app:create_app\(\) -b 0.0.0.0:8081 -w 3
   后台挂起启动
            nohup gunicorn myflaskapp.app:create_app\(\) -b 0.0.0.0:8081 -w 3 &

8： 启动
    邮件自动发送程序：        备注  如果这个邮件发送程序 已经启动过，不要再次启动， 多次启动会导致 邮件重复发送。  建议启动前先查看是否已经启动过该程序


部署完毕





使用文档

spi 相关程序启动说明

启动文档说明：
程序1:
1:  进入 路径  ：     cd /root/quatek_doc
2:  进入虚拟环境：    pipenv shell


文件处理方式：
只 把数据以此展示   不计算


