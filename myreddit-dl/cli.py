from reddit_client import RedditClient
from downloader import Downloader

DONT_RUN_THIS_FILE = ('This file is not intended to be run by itself. '
                      'See myreddit-dl -h for more information')

USER_NOT_FOUND = 'User not found. Make sure the `config.ini` file is correct.\n'


def print_debug(msg: str) -> None:
    print(f'[DEBUG] {msg}')

def print_done(msg: str) -> None:
    print(f'[DONE] {msg}')

def print_error(msg: str) -> None:
    print(f'[ERROR] {msg}')

def print_failed(msg: str) -> None:
    print(f'[FAILED] {msg}')

def print_file_added(filename: str) -> None:
    print(f'[ADDED] {filename}')

def print_already_exists(filename: str) -> None:
    print(f'[ALREADY EXISTS] {filename}')

def print_removing_file(filename: str) -> None:
    print(f'[REMOVING] {filename}')

def print_info(msg: str) -> None:
    print(f'[INFO] {msg}')

def print_editing(msg: str) -> None:
    print(f'[EDITING] {msg}')

def print_ok(msg: str) -> None:
    print(f'[OK] {msg}')


def print_warning(msg: str) -> None:
    print(f'[WARNING] {msg}')


def run_cli(args: dict) -> None:
    client = RedditClient(args)
    dl = Downloader(client)


if __name__ == '__main__':
    print_warning(DONT_RUN_THIS_FILE)
