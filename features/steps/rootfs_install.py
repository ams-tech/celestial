from behave import *
import utils
import filecmp
import celestial


@given('an {rootfs_format} formatted rootfs file')
def step_impl(context, rootfs_format):
    # Generate a small ext3 formatted file
    if rootfs_format == "ext3":
        context.rootfs_file = utils.make_ext3()
    elif rootfs_format == "ext2":
        context.rootfs_file = utils.make_ext2()
    else:
        raise ValueError("Unsupported rootfs type")


@given(u'a target device node')
def step_impl(context):
    # Generate a device node, the same size as the ext4_file above
    context.target_device_node = utils.make_device_node()


@when(u'we invoke celestial_rootfs_install with expected filesystem {fs_type}')
def step_impl(context, fs_type):
    if not hasattr(context, 'target_device_node'):
        node = '/dev/null'
    else:
        node = context.target_device_node
    try:
        context.celestial_rootfs_install_result = celestial.client.rootfs_install(
            rootfs_file=context.rootfs_file,
            device_node=node,
            expected_fs=fs_type
            )
    except ValueError as e:
        context.celestial_rootfs_install_result = e


@then(u'the ext3 file is burned into the target device node')
def step_impl(context):
    assert context.celestial_rootfs_install_result.returncode == 0
    assert filecmp.cmp(context.rootfs_file, context.target_device_node)


@given(u'a non-ext3 formatted rootfs file')
def step_impl(context):
    context.rootfs_file = utils.make_ext2()


@then(u'{name} fails with {exception}')
def step_impl(context, name, exception):
    result = getattr(context, "{}_result".format(name))
    assert isinstance(result, eval(exception))
