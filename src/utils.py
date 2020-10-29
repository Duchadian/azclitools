import os

from azure.cli.core import get_default_cli
from simple_term_menu import TerminalMenu


class PipelineItem:
    def __init__(self):
        self._result = None

    def __enter__(self):
        pass

    def __exit__(self, *args):
        pass


class AzCommandHandler(PipelineItem):
    def __init__(self):
        super().__init__()
        self.cli = get_default_cli()

    def _send_command(self, force=False):
        with open(os.devnull, 'w') as out:
            self.cli.invoke(self._command, out_file=out)
            result = self.cli.result

            if result.result:
                return result.result
            else:
                raise result.error

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


class MenuHandler(PipelineItem):
    def __init__(self, options: list):
        super().__init__()
        self._menu = TerminalMenu(options)

    @property
    def result(self):
        return self._result

    @result.getter
    def result(self):
        if not self._result:
            self._open_menu()
        return self._result

    def _open_menu(self) -> str: 
        self._result = self._menu.show()


def format_name(name: str) -> str:
    return " ".join(map(lambda s: s.capitalize(), name.split('_')))
