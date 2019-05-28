import os 
import subprocess
import shutil


LOCAL_DIR = os.path.dirname(os.path.realpath(__file__))
TEMP_DIRECTORY = os.path.join(LOCAL_DIR, "..", "..", ".tmp")


def set_up():
    os.makedirs(TEMP_DIRECTORY, exist_ok=True)


def tear_down():
    shutil.rmtree(TEMP_DIRECTORY)


def make_ext4(
        filename="test.ext4",
        fs_size_KB=10,
        random_file_size_KB=1
        ):
    """
    Creates a file with an ext4 partition of size fs_size
    with a random file of size random_file_size on the filesystem.
    """
    filepath = os.path.join(TEMP_DIRECTORY, filename)
    assert not os.path.isfile(filepath)
    retval = subprocess.run([
        'dd',
        "if=/dev/zero",
        "of='{}'".format(filepath),
        "bs=1K",
        "count={}".format(fs_size_KB)
        ])
    print("RETVAL: {}".format(retval))
