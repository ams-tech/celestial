from behave import *
import os

STEPS_DIRECTORY = os.path.dirname(os.path.realpath(__file__))


@given("the sample {subtype} file {filename}")
def step_impl(context, subtype, filename):
    """
    :param filename:
    :param subtype:
    :type context: behave.runner.Context
    """
    setattr(context,
            "sample_{}_file".format(subtype),
            os.path.join(STEPS_DIRECTORY, "..", "samples", context.feature.name, subtype, filename))
