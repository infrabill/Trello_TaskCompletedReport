#!/usr/bin/env python2
from argparse import ArgumentParser
from sys import argv
from trello import TrelloClient
from config import Config


def get_opts():
    ap = ArgumentParser(description="Lookup board and list IDs")
    ap.add_argument(
        '-c', '--conf',
        type=str,
        help="Configuration File"
    )
    ap.add_argument(
        'BOARD',
        type=str,
        help="The name of the board"
    )
    ap.add_argument(
        'LIST',
        type=str,
        help="The name of the list"
    )
    return ap.parse_args(argv[1:])


def find(trello, board_name, list_name):
    _board = find_board(trello, board_name)
    _list = find_list(_board, list_name)
    return _board, _list


def find_board(trello, board_name):
    for _board in trello.list_boards():
        print "DEBUG [BOARD]: {}".format(_board.name)
        if _board.name.lower() == board_name.lower():
            return _board


def find_list(board, list_name):
    for _list in board.get_lists(None):
        print "DEBUG [LIST]: {}".format(_list.name)
        if _list.name.lower() == list_name.lower():
            return _list


if __name__ == "__main__":
    opts = get_opts()
    conf = Config(opts.conf)
    t = TrelloClient(
        conf.get_trello_key(),
        conf.get_trello_key_secret(),
        conf.get_trello_oauth_key(),
        conf.get_trello_oauth_secret()
    )

    _board, _list = find(t, opts.BOARD, opts.LIST)
    print "[BOARD:{}]".format(_board.name)
    print "board_id = {}".format(_board.id)
    print "list_id = {}".format(_list.id)
