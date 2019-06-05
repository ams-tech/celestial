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


def copy_file_to_temp(path, target_subpath=""):
    """
    Copy the file at "path" to TEMP_DIRECTORY
    :param path:
    :param target_subpath: Add folders between TEMP_DIRECTORY and the copied file
    :return: the path of the new file
    """
    filename = os.path.basename(path)
    target_dir = os.path.join(TEMP_DIRECTORY, target_subpath)
    os.makedirs(target_dir, exist_ok=True)
    target_path = os.path.join(target_dir, filename)
    shutil.copyfile(path, target_path)
    return target_path


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


def make_ext(revision, filepath, fs_size_kb):
    """
    Create an ext 2,3, or 4 fs
    :param revision:
    :param filepath:
    :param fs_size_kb:
    :return:
    """
    if revision not in [2, 3, 4]:
        raise ValueError("Unsupported ext format")
    # Zero out the file
    make_zero_file(filepath, fs_size_kb)
    # Write an ext4 filesystem to that file
    retval = subprocess.run([
        'mkfs.ext{}'.format(revision),
        filepath,
    ])
    assert retval.returncode == 0
    return filepath


def make_ext2(
    filename="test_ext2.ext2",
    fs_size_kb=100
):
    """
    Creates a file with an ext3 partition of size fs_size
    :return:
    """
    filepath = os.path.join(TEMP_DIRECTORY, filename)
    return make_ext(2, filepath, fs_size_kb)


def make_ext3(
    filename="test_ext3.ext3",
    fs_size_kb=100
):
    """
    Creates a file with an ext3 partition of size fs_size
    """
    filepath = os.path.join(TEMP_DIRECTORY, filename)
    return make_ext(3, filepath, fs_size_kb)


def make_ext4(
    filename="test_ext4.ext4",
    fs_size_kb=100
):
    """
    Creates a file with an ext4 partition of size fs_size
    """
    filepath = os.path.join(TEMP_DIRECTORY, filename)
    return make_ext(4, filepath, fs_size_kb)


def prepend_temp_dir(expected_device_node):
    return os.path.join(TEMP_DIRECTORY, expected_device_node)
