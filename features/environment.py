import features.utils as utils


def before_scenario(context, scenario):
    utils.set_up()


def after_scenario(context, scenario):
    utils.tear_down()
