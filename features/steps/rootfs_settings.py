from behave import *


@when("we query the boot rootfs device")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When we query the boot rootfs device')


@then("the reported boot rootfs device is {expected_result}")
def step_impl(context, expected_result):
    """
    :param expected_result:
    :type context: behave.runner.Context
    """
    assert context.boot_rootfs_device_result == expected_result
