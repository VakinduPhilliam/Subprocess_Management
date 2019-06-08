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
# Run the command described by args.
# Wait for command to complete, then return a CompletedProcess instance.
#

#
# Older high-level API:
#
# subprocess.check_output(args, *, stdin=None, stderr=None, shell=False, cwd=None, encoding=None, errors=None, universal_newlines=None, timeout=None,
# text=None).
# Run command with arguments and return its output.
#

# 
# If the return code was non-zero it raises a CalledProcessError.
# The CalledProcessError object will have the return code in the returncode attribute and any output in the output attribute.
# 

#
# This is equivalent to:
# 

run(..., check=True, stdout=PIPE).stdout
