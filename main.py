import requests_cache

from src.utils import AzCommandHandler, choice_menu
from src.azclitools import commands

requests_cache.install_cache(
    cache_name='az_cache',
    backend='sqlite',
    expire_after=180
)


def format_name(name: str) -> str:
    return " ".join(map(lambda s: s.capitalize(), name.split('_')))


if __name__ == "__main__":
    choice = choice_menu([format_name(i) for i in commands])

    execute = commands[list(commands.keys())[choice]]

    cli = AzCommandHandler()
    cli.command = execute['az_data_command']
    filtered = map(execute['filter'], cli.result)

    menu_result = choice_menu(filtered)
    print(filtered)
    print(menu_result)
