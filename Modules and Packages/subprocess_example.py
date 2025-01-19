"""
The subprocess module lets you run external commands from within a Python script. Using
subprocess.run, you can execute a command and capture its output or error messages. This
is particularly useful for automating tasks or interacting with system utilities.
"""

import subprocess

# Run a command and capture the output
result = subprocess.run(["echo", "Hello World"], capture_output=True, text=True)
print(result.stdout) # Output: Hello World