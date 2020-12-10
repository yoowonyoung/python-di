from peewee import MySQLDatabase

from di.utils.logger import get_logger


class MysqlClient:
    def __init__(self, database, host, port, username, password):
        self.logger = get_logger(self.__class__.__name__)
        self.db = MySQLDatabase(
            database,
            host=host,
            port=int(port),
            user=username,
            password=password
        )
        self.db.connect()
        self.logger.debug(self.db)

    def get_database_instance(self):
        return self.db

    def __del__(self):
        if not self.db.is_closed():
            self.db.close()
