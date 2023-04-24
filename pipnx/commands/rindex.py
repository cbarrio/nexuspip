import os
from pipnx.logger import Logger


def request_nexus_package_versions(module_name: str):
    Logger.log(f"Available versions...{module_name}")

def exec(params: list):
    request_nexus_package_versions(params[0])