import os

TERMINAL_SIZE = os.get_terminal_size()

input(('=' * TERMINAL_SIZE.columns + '\n') * TERMINAL_SIZE.lines)

