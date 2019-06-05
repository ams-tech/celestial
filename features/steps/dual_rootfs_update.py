from behave import *
import celestial.client.rootfs
from features import utils

use_step_matcher("re")


@step("the rootfs device nodes are named (?P<dev1>.+) and (?P<dev2>.+)")
def step_impl(context, dev1, dev2):
    """
    :type context: behave.runner.Context
    :type dev1: str
    :type dev2: str
    """
    context.rootfs_device_node_1 = utils.make_device_node(dev1)
    if dev1 != dev2:
        context.rootfs_device_node_2 = utils.make_device_node(dev2)
    else:
        context.rootfs_device_node_2 = context.rootfs_device_node_1


@when("we update the dual boot rootfs")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    try:
        context.dual_boot_update_result = celestial.client.rootfs.dual_boot_update(
            rootfs_file=context.rootfs_file,
            dev_1=context.rootfs_device_node_1,
            dev_2=context.rootfs_device_node_2,
            expected_rootfs_format=context.rootfs_format,
            cmdline_file=context.sample_cmdline_file,
        )
    except ValueError as e:
        context.dual_boot_update_result = e


@step("the boot rootfs device is set to (?P<boot_device>.+)")
def step_impl(context, boot_device):
    """
    Set the boot device in the cmdline file
    :type context: behave.runner.Context
    :type boot_device: str
    """
    celestial.client.rootfs.set_boot_device(
        utils.prepend_temp_dir(boot_device),
        cmdline_file=context.sample_cmdline_file
    )
