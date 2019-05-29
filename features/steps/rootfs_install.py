from behave import *
import utils
import filecmp
import celestial


@given(u'an ext4 formatted file')
def step_impl(context):
    # Generate a small ext4 formatted file
    context.ext4_file = utils.make_ext4()


@given(u'a target device node')
def step_impl(context):
    # Generate a device node, the same size as the ext4_file above
    context.target_device_node = utils.make_device_node()


@when(u'we invoke celestial_rootfs_install')
def step_impl(context):
    celestial.client.rootfs_install(
        rootfs_file=context.ext4_file,
        device_node=context.target_device_node
        )


@then(u'the ext4 file is burned into the target device node')
def step_impl(context):
    assert filecmp.cmp(context.ext4_file, context.target_device_node)


@given(u'a non-ext4 formatted file')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a non-ext4 formatted file')


@then(u'the update fails')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the update fails')
