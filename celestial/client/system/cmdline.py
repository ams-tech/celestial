"""
Functions related to the cmdline file
"""


def load(cmdline_file):
    """
    Load the given file as a string
    :param cmdline_file:
    :return:
    """
    contents = ""
    with open(cmdline_file, 'r') as fpt:
        for l in fpt.readlines():
            contents += l
    return contents


def write(parameters, cmdline_file):
    """
    Create a cmdline file with the provided parameters
    Overwrite it if it exists
    :param parameters:
    :param cmdline_file:
    :return:
    """
    data = ""
    for key in parameters:
        if len(data) != 0:
            data += " "
        data += "{}={}".format(key, parameters[key])
    with open(cmdline_file, 'w') as fpt:
        fpt.write(data)


def get_parameters(cmdline_file):
    """
    Retrieve all of the parameters of the cmdline file
    :param cmdline_file:
    :return: a list of {key: , value: }
    """
    contents = load(cmdline_file)
    entries = contents.split(" ")
    parameters = {}
    for e in entries:
        kvp = e.split("=")
        if len(kvp) == 2:
            parameters[kvp[0]] = kvp[1]
    return parameters


def get_parameter(parameter_name, cmdline_file):
    """
    Retrieve a parameter from the provided cmdline file
    :param parameter_name:
    :param cmdline_file:
    :return:
    """
    parameters = get_parameters(cmdline_file)
    if "root" in parameters:
        return parameters[parameter_name]
    return None


def set_parameter(parameter_name, parameter_value, cmdline_file):
    """
    Set a parameter in the provided cmdline file.  Create it if it doesn't exist,
    overwrite it if it does exist
    :param parameter_name:
    :param parameter_value:
    :param cmdline_file:
    :return:
    """
    parameters = get_parameters(cmdline_file)
    parameters[parameter_name] = parameter_value
    write(parameters, cmdline_file)
