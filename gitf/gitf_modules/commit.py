import subprocess


def make_git_commit(CURRENT_WORKING_DIR, message):
    git_command_status = (
        "(git status --porcelain | grep '^ M' | awk '{print $2}') >"
        + f"{CURRENT_WORKING_DIR}/filePathModified.txt"
    )
    git_command_status = git_command_status.split(" ")
    git_command_add = ["git", "add", "."]
    git_command_commit = ["git", "commit", "-m", message]
    subprocess.run(git_command_status, capture_output=True, text=True)
    subprocess.run(git_command_add, capture_output=True, text=True)
    subprocess.run(git_command_commit, capture_output=True, text=True)
