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
# subprocess.getstatusoutput(cmd): 
# Return (exitcode, output) of executing cmd in a shell.
#

# 
# Execute the string cmd in a shell with Popen.check_output() and return a 2-tuple (exitcode, output).
# The locale encoding is used; see the notes on Frequently Used Arguments for more details.
#

# 
# A trailing newline is stripped from the output. The exit code for the command can be interpreted as the return code of subprocess.
#
# Example:
# 

subprocess.getstatusoutput('ls /bin/ls')

# OUTPUT: '(0, '/bin/ls')'

subprocess.getstatusoutput('cat /bin/junk')

# OUTPUT: '(1, 'cat: /bin/junk: No such file or directory')'

subprocess.getstatusoutput('/bin/junk')

# OUTPUT: '(127, 'sh: /bin/junk: not found')'

subprocess.getstatusoutput('/bin/kill $$')

# OUTPUT: '(-15, '')'
