from behave import *
import os
from features import utils

STEPS_DIRECTORY = os.path.dirname(os.path.realpath(__file__))


@given("the sample {subtype} file {filename}")
def step_impl(context, subtype, filename):
    """
    sets the "context.sample_{subtype}_file" attribute to "{filename}"
    :param filename:
    :param subtype:
    :type context: behave.runner.Context
    """
    file = os.path.join(STEPS_DIRECTORY, "..", "samples", subtype, filename)
    tmp_file = utils.copy_file_to_temp(file, target_subpath=os.path.join(context.feature.name, subtype))
    setattr(context, "sample_{}_file".format(subtype), tmp_file)
