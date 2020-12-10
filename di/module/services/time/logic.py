import datetime

from di.utils.logger import get_logger


class Logic:

    def __init__(self) -> None:
        self.logger = get_logger(self.__class__.__name__)

    def show_current_time(self):
        print(datetime.datetime.now())
        return datetime.datetime.now()

