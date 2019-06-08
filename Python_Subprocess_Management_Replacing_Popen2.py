# Python Subprocess Management
# subprocess — Subprocess management.
# The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.
# This module intends to replace several older modules and functions:
#
# Using the subprocess Module.
# The recommended approach to invoking subprocesses is to use the run() function for all use cases it can handle.
# For more advanced use cases, the underlying Popen interface can be used directly.
#

#
# subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, 
# encoding=None, errors=None, text=None, env=None, universal_newlines=None):
# Run the command described by args. Wait for command to complete, then return a CompletedProcess instance.
#


#
# Replacing Older Functions with the subprocess Module
#

#
# Replacing functions from the popen2 module
# 

#
# Note:
# 
# If the cmd argument to popen2 functions is a string, the command is executed through /bin/sh.
# If it is a list, the command is directly executed.
# 

(child_stdout, child_stdin) = popen2.popen2("somestring", bufsize, mode)

==>

p = Popen("somestring", shell=True, bufsize=bufsize,
          stdin=PIPE, stdout=PIPE, close_fds=True)

(child_stdout, child_stdin) = (p.stdout, p.stdin)
 

(child_stdout, child_stdin) = popen2.popen2(["mycmd", "myarg"], bufsize, mode)

==>

p = Popen(["mycmd", "myarg"], bufsize=bufsize,
          stdin=PIPE, stdout=PIPE, close_fds=True)

(child_stdout, child_stdin) = (p.stdout, p.stdin)
 
#
# popen2.Popen3 and popen2.Popen4 basically work as subprocess.Popen, except that:
# > Popen raises an exception if the execution fails.
# > the capturestderr argument is replaced with the stderr argument.
# > stdin=PIPE and stdout=PIPE must be specified.
# > popen2 closes all file descriptors by default, but you have to specify close_fds=True with Popen to guarantee this behavior on all platforms or past
#   Python versions.
#