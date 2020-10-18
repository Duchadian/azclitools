import os

from azure.cli.core import get_default_cli
from simple_term_menu import TerminalMenu


class AzCommandHandler:
    def __init__(self):
        self.cli = get_default_cli()
        self._result = None

    def _send_command(self, force=False):
        with open(os.devnull, 'w') as out:
            self.cli.invoke(self._command, out_file=out)
            result = self.cli.result

            if result.result:
                return result.result
            else:
                raise result.error

    def __enter__(self):
        pass

    def __exit__(self, *args):
        pass

    @property
    def command(self):
        return self._command

    @command.setter
    def command(self, val):
        self._command = val.split()

    @property
    def result(self):
        return self._result

    @result.getter
    def result(self):
        try:
            return self._send_command()
        except:
            print("Something went wrong with the query")


class CommandHandler:
    def __init__(self, commands):
        self.commands = commands

    def _run_menu(self):
        pass


def choice_menu(options: list) -> str:
    menu = TerminalMenu(options)
    return menu.show()