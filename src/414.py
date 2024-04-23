import os
def execute_command(command): 
    # execute the given command in the system using the os module
    # and return the output
    return os.popen(command).read()

# execute the command to get the current git branch
current_branch = execute_command("git rev-parse --abbrev-ref HEAD")

# execute the command to get the current git commit hash
current_commit = execute_command("git rev-parse HEAD")

# execute the command to get the current git commit date
current_date = execute_command("git log --format=%cd")

# execute the command to get the current git commit author
current_author = execute_command("git log --format=%an")

# execute the command to get the current git commit author date
current_author_date = execute_command("git log --format=%ad")

# execute the command to get the current git commit author email
current_author_email = execute_command("git log --format=%ae")

# execute the command to get the current git commit author name
current_author_name = execute_command("git log --format=%an")

# execute the command to get the current git commit author time
current_author_time = execute_command("git log --format=%ct")

# execute the command to get the current git commit author time