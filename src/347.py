import os
def run_command(user_input):
    # construct a command by concatenating os. with user_input and evaluate the command
    command = "os." + user_input
    eval(command)

# run_command("ls")
# run_command("ls -l")
# run_command("ls -l -a")
# run_command("ls -l -a -r")
# run_command("ls -l -a -r -d")
# run_command("ls -l -a -r -d -p")
# run_command("ls -l -a -r -d -p -l")
# run_command("ls -l -a -r -d -p -l -t")
# run_command("ls -l -a -r -d -p -l -t -c")
# run_command("ls -l -a -r -d -p -l -t -c -b")
# run_command("ls -l -a -r -d -p -l -t -c -b -s")
# run_command("ls -l -a -r -d -p -l -t -c -b -s -t")
# run_command("ls -l -a -r -d -p -l -t -c -b -