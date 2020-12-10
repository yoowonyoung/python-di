from di.module.cli.command import BaseCommand
from di.utils.logger import get_logger


class TimeCommand(BaseCommand):
    """showCurrentTime"""

    def __init__(self, time_service):
        super().__init__()
        self.logger = get_logger(self.__class__.__name__)
        self.time_service = time_service

    def command_parser(self, subparser):
        super().command_parser(subparser)

    def main(self, args):
        self.logger.info('Show Current Time')
        self.time_service.show_current_time()
