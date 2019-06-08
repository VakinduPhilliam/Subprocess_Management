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
#
# Replacing os.popen(), os.popen2(), os.popen3()
#
# 

(child_stdin, child_stdout) = os.popen2(cmd, mode, bufsize)

==>

p = Popen(cmd, shell=True, bufsize=bufsize,
          stdin=PIPE, stdout=PIPE, close_fds=True)

(child_stdin, child_stdout) = (p.stdin, p.stdout)
 

(child_stdin,
 child_stdout,
 child_stderr) = os.popen3(cmd, mode, bufsize)

==>

p = Popen(cmd, shell=True, bufsize=bufsize,
          stdin=PIPE, stdout=PIPE, stderr=PIPE, close_fds=True)

(child_stdin,
 child_stdout,
 child_stderr) = (p.stdin, p.stdout, p.stderr)
 

(child_stdin, child_stdout_and_stderr) = os.popen4(cmd, mode, bufsize)

==>

p = Popen(cmd, shell=True, bufsize=bufsize,
          stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)

(child_stdin, child_stdout_and_stderr) = (p.stdin, p.stdout)

#
# 
# Return code handling translates as follows:
#
# 

pipe = os.popen(cmd, 'w')

# ...

rc = pipe.close()

if rc is not None and rc >> 8:
    print("There were some errors")

==>

process = Popen(cmd, stdin=PIPE)

# ...

process.stdin.close()

if process.wait() != 0:

    print("There were some errors")
