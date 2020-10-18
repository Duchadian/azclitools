import os

import requests_cache
from azure.cli.core import get_default_cli
from simple_term_menu import TerminalMenu

requests_cache.install_cache(cache_name='az_cache', backend='sqlite', expire_after=180)


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


if __name__ == "__main__":
    cli = AzCommandHandler()
    cli.command="account list"

    print(cli.result)

    menu = TerminalMenu(['1', '2', '3'])
    choice = menu.show()
    print(choice)
