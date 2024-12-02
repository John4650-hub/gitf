from gitf.gitf_modules.push import pushFileModification
from gitf.gitf_modules.commit import make_git_commit
import os
import json
import argparse

CURRENT_WORKING_DIR = str(os.getcwd())
FILE_PATH = CURRENT_WORKING_DIR + "/.gitfConfig.json"


# returns true or false
def is_configFile_exists():
    if os.path.isfile(FILE_PATH):
        return True
    else:
        return False


def main():
    parser = argparse.ArgumentParser(
        description="""
        This is a utility to make commits to
         a github repository to specific files
         rather than the whole repository
        """,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("-t", type=str, help="your github personal access token")
    parser.add_argument(
        "-m",
        type=str,
        help="Simple message to commit the changes with",
        default="commited changes",
    )
    parser.add_argument(
        "--push",
        action="store_false",
        help="\nwhether you want to push a file from github repository",
        default=True,
    )
    parser.add_argument(
        "--save",
        action="store_true",
        help="\nSave the Owner's Name , Branch and Repository Name by default it's set",
        default=False,
    )

    if is_configFile_exists():
        with open(FILE_PATH, "r") as config:
            dbs = json.load(config)
        args = parser.parse_args()
        REPO_NAME = dbs["REPO_NAME"]
        REPO_OWNER = dbs["REPO_OWNER"]
        BRANCH = dbs["BRANCH"]
        TOKEN = args.t
        MESSAGE = args.m
        if args.push:
            make_git_commit(CURRENT_WORKING_DIR, MESSAGE)
            with open(CURRENT_WORKING_DIR + "/filePathModified.txt", "r") as fPaths:
                [
                    pushFileModification(
                        TOKEN, BRANCH, REPO_OWNER, REPO_NAME, path.strip(), MESSAGE
                    )
                    for path in fPaths.readlines()
                ]

    else:
        parser.add_argument("-r", type=str, help="github repository name")
        parser.add_argument("-w", type=str, help="owners name")
        parser.add_argument("-b", type=str, help="branch name")
        args = parser.parse_args()
        REPO_NAME = args.r
        REPO_OWNER = args.w
        BRANCH = args.b
        TOKEN = args.t
        MESSAGE = args.m
        if args.p:
            make_git_commit(CURRENT_WORKING_DIR, MESSAGE)
            with open(CURRENT_WORKING_DIR + "/filePathModified.txt", "r") as fPaths:
                [
                    pushFileModification(
                        TOKEN, BRANCH, REPO_OWNER, REPO_NAME, path.strip(), MESSAGE
                    )
                    for path in fPaths.readlines()
                ]
            if args.save:
                data = {}
                data["REPO_NAME"] = REPO_NAME
                data["REPO_OWNER"] = REPO_OWNER
                data["BRANCH"] = BRANCH
                with open(CURRENT_WORKING_DIR + "/.gitfConfig.json", "w") as gtfConfig:
                    json.dump(data, gtfConfig)
                with open(CURRENT_WORKING_DIR + "/.gitignore", "w") as ignoreFile:
                    ignoreFile.write("filePathModified.txt"+"\n" + ".gitfConfig.json")


if __name__ == "__main__":
    main()
