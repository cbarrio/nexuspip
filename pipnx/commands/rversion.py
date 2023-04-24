from pipnx.logger import Logger
from pipnx import __version__ 

def exec():
    Logger.log(f"pipnx {__version__}")