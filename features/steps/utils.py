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


def make_ext4(
        filename="test.ext4",
        fs_size_KB=100
        ):
    """
    Creates a file with an ext4 partition of size fs_size
    """
    filepath = os.path.join(TEMP_DIRECTORY, filename)
    assert not os.path.isfile(filepath)
    # Create a file of size fs_size_KB
    retval = subprocess.run([
        'dd',
        "if=/dev/zero",
        "of={}".format(filepath),
        "bs=1K",
        "count={}".format(fs_size_KB)
        ])
    assert retval.returncode == 0
    subprocess.run(['sync'])
    # Write an ext4 filesystem to that file
    retval = subprocess.run([
        'mkfs.ext4',
        filepath,
        ])
    assert retval.returncode == 0
    return filepath
