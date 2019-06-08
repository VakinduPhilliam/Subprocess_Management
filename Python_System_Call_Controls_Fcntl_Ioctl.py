# Python Fcntl 
# fcntl — The fcntl and ioctl system calls.
# This module performs file control and I/O control on file descriptors.
# It is an interface to the fcntl() and ioctl() Unix routines.
# All functions in this module take a file descriptor fd as their first argument.
# This can be an integer file descriptor, such as returned by sys.stdin.fileno(), or an io.IOBase object, such as sys.stdin itself, which provides
# a fileno() that returns a genuine file descriptor.
#
# fcntl.ioctl(fd, request, arg=0, mutate_flag=True): 
# This function is identical to the fcntl() function, except that the argument handling is even more complicated.
# 
# The request parameter is limited to values that can fit in 32-bits. Additional constants of interest for use as the request argument can be found in the
# termios module, under the same names as used in the relevant C header files.
# The parameter arg can be one of an integer, an object supporting the read-only buffer interface (like bytes) or an object supporting the read-write buffer
# interface (like bytearray).
#

#
# An example:
#

import array, fcntl, struct, termios, os

os.getpgrp()

# OUTPUT: '13341'

struct.unpack('h', fcntl.ioctl(0, termios.TIOCGPGRP, "  "))[0]

# OUTPUT: '13341'

buf = array.array('h', [0])

fcntl.ioctl(0, termios.TIOCGPGRP, buf, 1)

# OUTPUT: '0'

buf

# OUTPUT: 'array('h', [13341])'
