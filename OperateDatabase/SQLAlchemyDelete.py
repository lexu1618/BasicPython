#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   SQLAlchemyDelete.py
@Time    :   2019/11/5 21:09
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from OperateDatabase.SQLAlchemyConnect import News
from OperateDatabase.SQLAlchemyConnect import connect_database
from sqlalchemy.orm import sessionmaker


class DeleteData(object):
    def __init__(self):
        Session = sessionmaker(bind=connect_database().engine)
        self.session = Session()

    def delete_data(self):
        """删除数据"""
        data = self.session.query(News).filter_by(title='news4')
        self.session.delete(data)
        self.session.commit()


if __name__ == "__main__":
    dd = DeleteData()
    dd.delete_data()
