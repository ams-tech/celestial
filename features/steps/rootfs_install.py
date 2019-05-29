from behave import *
import utils
import filecmp
import celestial


@given(u'an ext3 formatted file')
def step_impl(context):
    # Generate a small ext4 formatted file
    context.ext3_file = utils.make_ext3()


@given(u'a target device node')
def step_impl(context):
    # Generate a device node, the same size as the ext4_file above
    context.target_device_node = utils.make_device_node()


@when(u'we invoke celestial_rootfs_install')
def step_impl(context):
    if not hasattr(context, 'target_device_node'):
        node = '/dev/null'
    else:
        node = context.target_device_node
    try:
        context.celestial_rootfs_install_result = celestial.client.rootfs_install(
            rootfs_file=context.ext3_file,
            device_node=node
            )
    except ValueError as e:
        context.celestial_rootfs_install_result = e


@then(u'the ext3 file is burned into the target device node')
def step_impl(context):
    assert context.celestial_rootfs_install_result.returncode == 0
    assert filecmp.cmp(context.ext3_file, context.target_device_node)


@given(u'a non-ext3 formatted file')
def step_impl(context):
    context.ext3_file = utils.make_non_ext4()


@then(u'{name} fails with {exception}')
def step_impl(context, name, exception):
    result = getattr(context, "{}_result".format(name))
    assert isinstance(result, eval(exception))
