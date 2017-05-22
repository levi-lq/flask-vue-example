# coding=utf-8
"""
desc:   app管理脚本
author: levi-lq
date:   2017-05-23

"""

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from api_rest import app

manager = Manager(app)
# migrate database command
manager.add_command("db", MigrateCommand)


if __name__ == "__main__":
    manager.run()