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
# Replacing os.system()
# 

sts = os.system("mycmd" + " myarg")

# becomes

sts = call("mycmd" + " myarg", shell=True)

# 
# Notes:
# > Calling the program through the shell is usually not required.
#

# 
# A more realistic example would look like this:
# 

try:
    retcode = call("mycmd" + " myarg", shell=True)

    if retcode < 0:
        print("Child was terminated by signal", -retcode, file=sys.stderr)

    else:
        print("Child returned", retcode, file=sys.stderr)

except OSError as e:

    print("Execution failed:", e, file=sys.stderr)
