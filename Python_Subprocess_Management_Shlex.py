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
# Popen Constructor:
# The underlying process creation and management in this module is handled by the Popen class.
# It offers a lot of flexibility so that developers are able to handle the less common cases not covered by the convenience functions.
#
# class subprocess.Popen(args, bufsize=-1, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=True, shell=False, cwd=None,
# env=None, universal_newlines=None, startupinfo=None, creationflags=0, restore_signals=True, start_new_session=False, pass_fds=(), *, encoding=None,
# errors=None, text=None):
#
# Execute a child program in a new process. On POSIX, the class uses os.execvp()-like behavior to execute the child program.
# On Windows, the class uses the Windows CreateProcess() function.
#

#
# Note:
# shlex.split() can be useful when determining the correct tokenization for args, especially in complex cases:
# 

import shlex, subprocess

command_line = input()

# OUTPUT: '/bin/vikings -input eggs.txt -output "spam spam.txt" -cmd "echo '$MONEY'"'

args = shlex.split(command_line)

print(args)

# OUTPUT: '['/bin/vikings', '-input', 'eggs.txt', '-output', 'spam spam.txt', '-cmd', "echo '$MONEY'"]'

p = subprocess.Popen(args) # Success!
