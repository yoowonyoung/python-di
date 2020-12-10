import sys
from abc import ABCMeta, abstractmethod
from argparse import RawTextHelpFormatter


class BaseCommand(metaclass=ABCMeta):
    """Basic Command

    This is a basic command"""

    def __init__(self):
        pass

    def command_parser(self, subparser):
        splitted = self.__doc__.split('\n')
        self.parser = subparser.add_parser(name=splitted[0],
                                           help=splitted[-1].strip(),
                                           description='\n'.join(splitted[1:]),
                                           formatter_class=RawTextHelpFormatter)
        self.parser.set_defaults(method=self.main)

    @abstractmethod
    def main(self, args):
        pass


class CommandProccessor:

    def __init__(self, parser, subcommands, version):
        self.parser = parser
        self.parser.add_argument('-V', '--version', action='version', version=version)
        self.parser.format_usage = parser.format_help

        subparsers = self.parser.add_subparsers(title='commands', dest='commands')
        subparsers.required = True

        for subcommand in subcommands:
            subcommand.command_parser(subparser=subparsers)

        args = parser.parse_args(sys.argv[1:])
        args.method(args)
