import os
import subprocess

from celestial.strings import Filesystems
from celestial.client.system import cmdline


def get_fs_types(path):
    """
    Fetch a list of possible filesystem types
    :param path:
    :return: a list of strings with the possible filesystem type, else None
    """
    if not os.path.exists(path):
        return None
    output = subprocess.check_output(
        ['''(eval $(blkid {} | awk ' {{ print $3 }} '); echo $TYPE)'''.format(path)],
        shell=True,
        executable='/bin/bash').decode().rstrip()
    if output == "":
        retval = []
    elif output == Filesystems.EXT2:
        # ext3 filesystems misidentify as ext2.  Consider both as possible outputs
        retval = [Filesystems.EXT2, Filesystems.EXT3]
    else:
        retval = [output]
    return retval


def install(rootfs_file, device_node, block_size_kb=10, expected_fs=Filesystems.NONE):
    """
    Install rootfs_file into device_node
    """
    if expected_fs is not None:
        fs_types = get_fs_types(rootfs_file)
        if expected_fs not in fs_types:
            raise ValueError("rootfs_file is type {}, expected {}".format(rootfs_file, expected_fs))
    result = subprocess.run([
        'dd',
        'if={}'.format(rootfs_file),
        'of={}'.format(device_node),
        'bs={}K'.format(block_size_kb)
    ])
    if result.returncode != 0:
        raise RuntimeError("Failed to update {} with {}".format(device_node, rootfs_file))
    return result


def get_boot_device(cmdline_file="/proc/cmdline"):
    """
    Retrieve the "root" parameter of "/proc/cmdline"
    :param cmdline_file: The location of the cmdline file (that we booted with)
    :return:
    """
    return cmdline.get_parameter("root", cmdline_file)


def set_boot_device(boot_device, cmdline_file="/boot/cmdline"):
    """
    Update the "root" parameter of the "cmdline_file" to "boot_device"
    :param boot_device:
    :param cmdline_file:  The location of the boot partition's commandline file
    :return:
    """
    cmdline.set_parameter("root", boot_device, cmdline_file)


def dual_boot_update(rootfs_file, dev_1, dev_2, cmdline_file="/boot/cmdline", expected_rootfs_format=None):
    """

    :param rootfs_file: The filesystem to be installed
    :param expected_rootfs_format: The expected rootfs format
    :param cmdline_file: The location of the boot partition's commandline file
    :param dev_1: the first rootfs device node in the dual-boot configuration
    :param dev_2: the second rootfs device node in the dual-boot configuration
    :return:
    """
    current_boot_dev = get_boot_device(cmdline_file=cmdline_file)
    if current_boot_dev == dev_1:
        target_boot_dev = dev_2
    elif current_boot_dev == dev_2:
        target_boot_dev = dev_1
    else:
        raise ValueError("current rootfs '{}' does not match dev_1 or dev_2".format(current_boot_dev))

    result = install(rootfs_file, target_boot_dev, expected_fs=expected_rootfs_format)


    set_boot_device(target_boot_dev, cmdline_file=cmdline_file)
