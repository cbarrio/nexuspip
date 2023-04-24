from enum import Enum

class LColor(Enum):
    RED='\033[0;31m'
    YELLOW='\033[1;33m'
    GRAY='\033[1;30m'
    CYAN='\033[1;36m'
    NC='\033[0m'

class Logger:

    @staticmethod
    def log(message: str):
        print(message)

    @staticmethod
    def debug(message: str):
        Logger.log(Logger.colorg(LColor.GRAY, f"DEBUG: {message}"))
    
    @staticmethod
    def header(message: str):
        Logger.log(Logger.colorg(LColor.CYAN, message))

    @staticmethod
    def error(message: str):
        Logger.log(Logger.colorg(LColor.RED, f"ERROR: {message}"))

    @staticmethod
    def exception(exception_list: list):
        message = ''.join(exception_list)
        Logger.log(Logger.colorg(LColor.RED, message))

    @staticmethod
    def warning(message: str):
        Logger.log(Logger.colorg(LColor.YELLOW, f"WARNING: {message}"))

    @staticmethod
    def colorg(color: LColor, message: str):
        return f"{color.value}{message}{LColor.NC.value}"
