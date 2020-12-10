from di.module.services import BaseService
from di.utils.logger import get_logger


class TimeService(BaseService):

    def __init__(self, logic):
        self.logger = get_logger(self.__class__.__name__)
        self.logic = logic

    def show_current_time(self):
        self.logger.info('Get Current Time')
        return self.logic.show_current_time()
