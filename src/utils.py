import os

from azure.cli.core import get_default_cli


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
