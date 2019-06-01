"""
Functions related to the cmdline file
"""


def get_parameter(parameter_name, cmdline_file):
    contents = ""
    with open(cmdline_file, 'r') as fpt:
        for l in fpt.readlines():
            contents += l
    entries = contents.split(" ")
    for e in entries:
        kvp = e.split("=")
        if kvp[0] == parameter_name:
            return kvp[1]
    return None




