from __future__ import unicode_literals

import sys
from textwrap import dedent
from time import sleep

from IPython.core.getipython import get_ipython

from six.moves import input
# from IPython.core.prompts import PromptManager
from IPython.terminal.prompts import Prompts, Token
from traitlets.config import get_config

# from IPython.terminal.prompts import Prompts, Token
# import os
from IPython.core.interactiveshell import InteractiveShell


class ColorEncoding(object):
    """
    Color encodings for the terminal
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'  # Yellow
    FAIL = '\033[91m'  # Red
    ENDC = '\033[0m'  # End Encoding
    BOLD = '\033[1m'
    FAINT = '\033[2m'  # Not widely supported
    UNDERLINE = '\033[4m'

    @classmethod
    def wrap(cls, enc_name, my_string):
        enc = getattr(cls, enc_name.upper())
        return enc + my_string + cls.ENDC


def __warn_shell():
    """
    Print a warning and change the prompt depending on the shell being used
    """

    if sys.argv[1] == 'shell_plus':
        _warn_msg = dedent("""
        #######################################################################
        LOL....libtard. Are you ready for the Trump Train?
        #######################################################################
        """)
        print(ColorEncoding.wrap('fail', _warn_msg))
        val = input(
            ColorEncoding.wrap('warning', 'Are you sure? [y]/n : ')
        )
        if val and val.lower() != 'y':
            print(ColorEncoding.wrap('fail', "\nNothing matters\n"))
            sys.exit()
        else:
            print( ColorEncoding.wrap(
                'bold', ColorEncoding.wrap('okblue',"\nW O w\n")
            ))
    elif sys.argv[1] == 'safe_shell':
        print(ColorEncoding.wrap('okblue', "\nYou are safe here\n"))

# This occurs on import, because it was the only way to inject
# a message into the shell_plus prompt
__warn_shell()
