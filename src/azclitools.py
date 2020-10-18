import requests_cache
from simple_term_menu import TerminalMenu

from src.utils import AzCommandHandler

requests_cache.install_cache(cache_name='az_cache', backend='sqlite', expire_after=180)

def choice_menu(options: list) -> str:
    menu = TerminalMenu(options)
    return options[menu.show()]


if __name__ == "__main__":
    cli = AzCommandHandler()
    cli.command="account list"

    print(cli.result)

    choice = choice_menu('dit is een test'.split())
    print(choice)
