# -*- coding: utf-8 -*-

from peewee import *
from log import logger

db = MySQLDatabase("teletraan_test_project", host="127.0.0.1", port=3306, user="root", passwd="root123")
db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class TakeHomeOcrModel(BaseModel):
    id = BigIntegerField(primary_key=True, sequence=True)
    content = TextField()

    class Meta:
        db_table = 'take_home_ocr'

    @staticmethod
    def insert_data(data):
        logger.info("start insert data")
        try:
            with db.atomic():
                insert_sql = TakeHomeOcrModel.insert_many(data)
                insert_sql.execute()
            if insert_sql:
                logger.info("insert data success")
        except Exception as e:
            logger.error("insert data error: {}".format(e))

