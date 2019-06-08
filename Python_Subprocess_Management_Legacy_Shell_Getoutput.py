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
# Legacy Shell Invocation Functions:
# This module also provides the following legacy functions from the 2.x commands module.
# These operations implicitly invoke the system shell and none of the guarantees described above regarding security and exception handling consistency are
# valid for these functions.
#

#
# subprocess.getoutput(cmd): 
# Return output (stdout and stderr) of executing cmd in a shell.
#

# 
# Like getstatusoutput(), except the exit code is ignored and the return value is a string containing the command’s output.
#
# Example:
# 

subprocess.getoutput('ls /bin/ls')

# OUTPUT: '/bin/ls'
