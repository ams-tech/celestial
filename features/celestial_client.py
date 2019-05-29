# Wrappers for the Cestial client scripts
import subprocess


def rootfs_install(rootfs_file, device_node, block_size_KB=10):
    result = subprocess.run([
        'dd',
        'if={}'.format(rootfs_file),
        'of={}'.format(device_node),
        'bs={}K'.format(block_size_KB)
    ])
    assert result.returncode == 0
