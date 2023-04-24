import traceback
from pipnx.logger import Logger
from pipnx.commands import rinstall, rlist, runinstall, rindex, rhelp, rversion, pip

def main(argv):
    Logger.debug(argv)
    if len(argv) > 0:
        try:
            command = argv[0]
            params = argv[1:]
            if command == 'rinstall':
                rinstall.exec(params) 
            elif command == 'rlist':
                rlist.exec(params)
            elif command == 'runinstall':
                runinstall.exec(params) 
            elif command == 'rindex':
                rindex.exec(params) 
            elif command == 'rhelp':
                rhelp.exec() 
            elif command == 'rversion':
                rversion.exec() 
            else:
                pip.exec(argv)
        except Exception:
            Logger.exception(traceback.format_exc())
            return 1
    else:
        rhelp.exec() 
    return 0
