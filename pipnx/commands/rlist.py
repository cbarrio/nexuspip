
import os
from pipnx.logger import Logger
from pipnx.commands.pip import exec as pip_exec

virtual_env_path = os.environ.get('VIRTUAL_ENV',"")

def installed_versions(module_name: str):
    try:
        return sorted(os.listdir(os.path.join(virtual_env_path, "nexus", module_name)))
    except:
        return []

def exec(params: list):
    module_list = sorted(os.listdir(os.path.join(virtual_env_path, "nexus")))
    raw_modules = []
    raw_versions = []

    for module in module_list:
        version_list = installed_versions(module)
        for version in version_list:
            raw_modules.append(module)
            raw_versions.append(version)
    max_line = len(max(raw_modules, key = len))
    total_line = max_line + max_line + 1

    Logger.header(f"{'-'*total_line} nexus cache")
    Logger.log(f"{'Package':<{max_line}} Version")
    Logger.log(f"{'-'*max_line} {'-'*7}")

    for name, version in zip(raw_modules, raw_versions):
        Logger.log(f"{name:<{max_line}} {version}")
    
    if len(params) > 0 and params[0] in ['-a', '--all']:
        Logger.header(f"{'-'*total_line} python")
        pip_exec(['list'])
