from behave import *

use_step_matcher("re")


@step("the rootfs device nodes are (?P<dev1>.+) and (?P<dev2>.+)")
def step_impl(context, dev1, dev2):
    """
    :type context: behave.runner.Context
    :type dev1: str
    :type dev2: str
    """
    context.rootfs_device_node_1 = dev1
    context.rootfs_device_node_2 = dev2


@when("we update the dual boot rootfs")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When we update the dual boot rootfs')

