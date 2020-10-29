import requests_cache

from src.utils import AzCommandHandler, MenuHandler, format_name
from src.azclitools import commands

requests_cache.install_cache(
    cache_name='az_cache',
    backend='sqlite',
    expire_after=180
)

if __name__ == "__main__":
    choice = MenuHandler(
        options=[format_name(i) for i in commands]
    ).result

    execute = commands[list(commands.keys())[choice]]
    print(execute)

    cli = AzCommandHandler()
    cli.command = execute['az_data_command']
    filtered = map(execute['filter'], cli.result)

    # menu_result = choice_menu(filtered)
    print(filtered)
    # print(menu_result)
