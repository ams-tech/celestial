# Wrappers for the Celestial client scripts
import subprocess
import os


class Filesystems:
    EXT4 = "ext4"
    NONE = None


def get_fs_type(path):
    """
    Attempt to determine the filesystem type of path
    :param path:
    :return: a string with the filesystem name, else None
    """
    if not os.path.exists(path):
        return None
    return subprocess.check_output('''(eval $(blkid {} | awk ' {{ print $3 }} '); echo $TYPE)'''.format(path)).rstrip()


def rootfs_install(rootfs_file, device_node, block_size_kb=10, expected_fs=None):
    """
    Install rootfs_file into device_node
    """
    result = subprocess.run([
        'dd',
        'if={}'.format(rootfs_file),
        'of={}'.format(device_node),
        'bs={}K'.format(block_size_kb)
    ])
    return result
