#!/usr/bin/env python2
from argparse import ArgumentParser
from sys import argv
from config import Config


def get_opts():
    ap = ArgumentParser(
        description="Generate OAuth keys for interacting with remote services"
    )
    ap.add_argument(
        '-c', '--config',
        type=str,
        help="Path to the configuration file",
        required=True
    )
    ap.add_argument(
        'ACTION',
        type=str,
        choices=['init-trello', 'init-drive'],
        help="Select the action to execute"
    )
    ap.add_argument(
        'KEY',
        type=str,
        help="The API Key for the service"
    )
    ap.add_argument(
        'SECRET',
        type=str,
        help="The API Secret for the service"
    )
    return ap.parse_args(argv[1:])


if __name__ == "__main__":
    opts = get_opts()
    config = Config(opts.config)
    if opts.ACTION == 'init-trello':
        config.init_trello(
            opts.KEY,
            opts.SECRET
        )
