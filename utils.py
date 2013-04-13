from random import randint
import shlex
from subprocess import Popen, PIPE, STDOUT


def get_urandom_password(min=8, max=8):
    """
    Get data from /dev/urandom .
    """
    assert min <= max
    #
    length = randint(min, max)
    li = []
    with open("/dev/urandom") as f:
        while len(li) < length:
            c = f.read(1)
            if c.isalnum():
                li.append(c)

    return ''.join(li)


def get_simple_cmd_output(cmd, stderr=STDOUT):
    """Execute a simple external command and get its output.

    The command contains no pipes. Error messages are
    redirected to the standard output by default.
    """
    args = shlex.split(cmd)
    return Popen(args, stdout=PIPE, stderr=stderr).communicate()[0]