import steps.utils as utils


def before_scenario(context, scenario):
    utils.set_up(context)


def after_scenario(context, scenario):
    utils.tear_down(context)