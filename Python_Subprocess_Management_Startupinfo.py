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
# class subprocess.STARTUPINFO(*, dwFlags=0, hStdInput=None, hStdOutput=None, hStdError=None, wShowWindow=0, lpAttributeList=None):
# Partial support of the Windows STARTUPINFO structure is used for Popen creation. The following attributes can be set by passing them as keyword-only
# arguments.
# 

#
# dwFlags 
# A bit field that determines whether certain STARTUPINFO attributes are used when the process creates a window.
# 

si = subprocess.STARTUPINFO()

si.dwFlags = subprocess.STARTF_USESTDHANDLES | subprocess.STARTF_USESHOWWINDOW
