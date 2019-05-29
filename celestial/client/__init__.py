# Wrappers for the Celestial client scripts
import subprocess


def get_fs_type(path):
    """
    Attempt to determine the filesystem type of path
    :param path:
    :return: a string with the filesystem name, else None
    """


def rootfs_install(rootfs_file, device_node, block_size_kb=10):
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
