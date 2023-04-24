import os
from pipnx.logger import Logger


def install_nexus_package(module_name: str):
    Logger.log(f"Descargando...{module_name}")

def exec(params: list):
    if params:
        if params[0] in ['-r', '--requirement']:
            if len(params) > 1:
                file_name = params[1]
                file_pah, file_extension = os.path.splitext(file_name)
                if file_extension == '.nx':
                    with open(file_name, 'r') as file:
                        data = [line.strip() for line in file]
                        for line in data:
                            install_nexus_package(line)
                else:
                    Logger.error("Invalid file extension, expected .nx file")
            else:
                Logger.error("Missing requirements file path")
        else:
            install_nexus_package(params[0])
    else:
        Logger.error("Missing module name")