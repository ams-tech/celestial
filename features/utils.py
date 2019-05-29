import os
import subprocess
import shutil
from behave import fixture


LOCAL_DIR = os.path.dirname(os.path.realpath(__file__))
TEMP_DIRECTORY = os.path.join(LOCAL_DIR, "..", "..", ".tmp")


def set_up():
    os.makedirs(TEMP_DIRECTORY, exist_ok=True)


def tear_down():
    shutil.rmtree(TEMP_DIRECTORY)


def make_zero_file(filepath, file_size_kb):
    """
    Create a zeroed out file of size file_size_KB at filepath
    """
    assert not os.path.isfile(filepath)
    # Create a file of size fs_size_KB
    retval = subprocess.run([
        'dd',
        "if=/dev/zero",
        "of={}".format(filepath),
        "bs=1K",
        "count={}".format(file_size_kb)
        ])
    assert retval.returncode == 0


def make_device_node(
    filename="test_node",
    node_size_kb=100
):
    """
    Create a fake device node of size node_size_KB at the given filename
    """
    filepath = os.path.join(TEMP_DIRECTORY, filename)
    make_zero_file(filepath, node_size_kb)
    return filepath


def make_non_ext4(
    filename="test_non_ext4.ext4",
    fs_size_kb=100
):
    """
    create a non ext4 file.  consider passing types to this
    :return:
    """
    filepath = os.path.join(TEMP_DIRECTORY, filename)
    # Zero out the file
    make_zero_file(filepath, fs_size_kb)
    # Write an ext4 filesystem to that file
    retval = subprocess.run([
        'mkfs.ext2',
        filepath,
    ])
    assert retval.returncode == 0
    return filepath


def make_ext3(
    filename="test_ext4.ext4",
    fs_size_kb=100
):
    """
    Creates a file with an ext4 partition of size fs_size
    """
    filepath = os.path.join(TEMP_DIRECTORY, filename)
    # Zero out the file
    make_zero_file(filepath, fs_size_kb)
    # Write an ext4 filesystem to that file
    retval = subprocess.run([
        'mkfs.ext4',
        filepath,
        ])
    assert retval.returncode == 0
    return filepath
