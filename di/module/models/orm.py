from datetime import datetime

from peewee import DatabaseProxy, Model, CharField, DateTimeField, BooleanField, IntegerField, ForeignKeyField

from di.utils.logger import get_logger

database_proxy = DatabaseProxy()


def make_table_name(model_class):
    model_name = model_class.__name__
    return model_name + 's'


def initialize_orm(database):
    logger = get_logger('ORM')
    logger.debug('Initialize ORM : bind db with model')
    database_proxy.initialize(database)
    create_tables()


def create_tables():
    logger = get_logger('ORM')
    logger.debug('Create tables')
    database_proxy.create_tables(
        [
            #Table Name
        ]
    )


class BaseModel(Model):
    class Meta:
        database = database_proxy
        table_function = make_table_name

