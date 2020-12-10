from mongoengine import connect

from di.utils.logger import get_logger


class MongoDBClient:

    def __init__(self, host, port, database, username, password):
        self.logger = get_logger(self.__class__.__name__)
        self.connection = connect(db=database,
                                  host=host,
                                  port=port,
                                  username=username,
                                  password=password)
        self.logger.debug(self.connection)

    def get_database_instance(self):
        return self.connection
