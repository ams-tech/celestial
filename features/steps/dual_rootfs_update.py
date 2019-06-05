from behave import *
import celestial.client.rootfs

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
    try:
        context.dual_boot_update_result = celestial.client.rootfs.dual_boot_update(
            expected_fs=context.rootfs_format,
            cmdline_file=context.sample_cmdline_file,
            dev_1=context.rootfs_device_node_1,
            dev_2=context.rootfs_device_node_2,
        )
    except ValueError as e:
        context.dual_boot_update_result = e

