import pty
from pipnx.logger import Logger

def pty_command(args: list):
    Logger.debug(args)
    pty.spawn(args)

def exec(params: list=[]):
    return pty_command(['pip'] + params)
