import subprocess
import os


def make_git_commit(CURRENT_WORKING_DIR, message):
    # Ensure the working directory is valid
    if not os.path.isdir(CURRENT_WORKING_DIR):
        raise ValueError(f"Invalid directory: {CURRENT_WORKING_DIR}")

    # Change the current working directory to the specified directory
    original_cwd = os.getcwd()
    os.chdir(CURRENT_WORKING_DIR)

    try:
        # Check for modified files
        git_command_status = ["git", "status", "--porcelain"]
        result = subprocess.run(git_command_status, capture_output=True, text=True)

        # Write modified file paths to a text file
        with open("filePathModified.txt", "w") as f:
            for line in result.stdout.splitlines():
                if line.startswith(" M"):
                    f.write(line[3:] + "\n")

        # Add all changes to the staging area
        git_command_add = ["git", "add", "."]
        subprocess.run(git_command_add, capture_output=True, text=True)

        # Commit the changes with the provided message
        git_command_commit = ["git", "commit", "-m", message]
        subprocess.run(git_command_commit, capture_output=True, text=True)
    finally:
        # Change back to the original working directory
        os.chdir(original_cwd)
