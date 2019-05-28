from behave import *
import utils


@given(u'an ext4 formatted file')
def step_impl(context):
    # Generate a small ext4 formatted file
    context.ext4_file = utils.make_ext4()


@given(u'a target device node')
def step_impl(context):
    context.device_node = utils.make_device_node()


@when(u'we invoke rootfs device node update')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we invoke rootfs device node update')


@then(u'the ext4 file is burned into the target device node')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the ext4 file is burned into the target device node')


@given(u'a non-ext4 formatted file')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a non-ext4 formatted file')


@then(u'the update fails')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the update fails')
