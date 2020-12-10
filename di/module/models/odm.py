from datetime import datetime

from mongoengine import Document, StringField, DateTimeField, BooleanField, IntField, ReferenceField

from di.utils.logger import get_logger


def initialize_odm(connect):
    logger = get_logger('ODM')
    logger.debug('Initialize ODM : bind db with model')


class BaseMixin(object):
    meta = {
        'collection': lambda c: c.__name__.lower(),
        'allow_inheritance': True
    }
