import os
from pipnx.logger import Logger
from pipnx.commands.rlist import installed_versions

from pkg_resources import parse_version as p_version

def uninstall_nexus_package(module_name: str):
    Logger.log(f"Uninstall...{module_name}")
    operators = ['~=','==','<=','>=','<','>']
    name = module_name
    operator = None
    version = None
    for test_operator in operators:
        index = module_name.find(test_operator)
        if (index > -1):
            name = module_name[0:index]
            operator = test_operator
            version = module_name[index+len(test_operator):]
            break
    Logger.debug(f"name {name} op {operator} ver {version}")
    version_list = installed_versions(name)
    if not version_list:
        Logger.error(f"Module {module_name} is not installed")
    else:
        versions_to_delete = []
        for installed_version in version_list:
            string_condition = f"p_version('{installed_version}'){operator}p_version('{version}')"
            if not operator or eval(string_condition):
                versions_to_delete.append(installed_version)

        Logger.log("This versions will be removed from nexus cache:")
        Logger.log(f"    {name} {versions_to_delete}")
        txt = input("Delete? (y/n) ")


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
                            uninstall_nexus_package(line)
                else:
                    Logger.log("Invalid file extension, expected .nx file")
            else:
                Logger.log("Missing requirements file path")
        else:
            uninstall_nexus_package(params[0])
    else:
        Logger.log("Missing module name")