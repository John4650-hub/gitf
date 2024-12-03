##Gitf
This is a utility program to aid in modifying single file in a chosen directory

```bash
gitf --help
usage: gitf [-h] [-t T] [-m M] [--push] [--save] [-r R]
               [-w W] [-b B]

This is a utility to make commits to a github repository to
specific files rather than the whole repository

options:
  -h, --help  show this help message and exit
  -t T        your github personal access token (default: None)
  -m M        Simple message to commit the changes with
              (default: commited changes)
  --save      Save the Owner's Name , Branch and Repository Name
              by default it's set (default: False)
  -r R        github repository name (default: None)
  -w W        owners name (default: None)
  -b B        branch name (default: None)
```
### REASON
I find it always painful to clone the whole repoaitory when all i need is to make a change in one file, this discourages me from contributing to bigger opensource projects.

I also code sometimes using my phone using Termux.
This utility program has been written to aid in modifying specific files which are in one of the repositories owned by the user
### REQUIREMENTS
- git
- requests

Install requests using
```bash
pip install requests
```

### USAGE
Before using gitf make sure you create a new directory
Then enter the new directory and run `git init`
RUN THE FOLLOWING COMMAND

```bash
touch .gitignore && git add .gitignore && git commit -m "created .igitignore"
```

Create the file you want to modify with the same name and path for example
if in your remote github repository you have the following directory structure

```bash
├── .git
├── .github
├── README.md
├── gitf
│   ├── __init__.py
│   ├── gitf_modules
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── commit.py
│   │   └── push.py
│   └── main.py
├── requirements.txt
└── setup.py
```
If you want to modify `push.py`, you need to also create the sameb path in your new folder called 
```bash
mkdir -p gitf/gitf_modules
touch push.py
```
After creating the file modify it as you want , [you can also copy the code from you repository into the file and modify it as required.
Then run one of the commands below as required
#### simple usage

```bash
gitf -t [GITHUB_PERSONAL_TOKEN] -w [GITHUB_USER_NAME] -r [USER_GITHUB_REPOSITORY] -b [BRANCH_NAME] -m "[message_to_attach to changes made]" 
```
If you include `--save`, a file called `.gitfConfig.json` is automatically created and contains the `GITHUB_USER_NAME`, `USER_GITHUB_REPOSITORY`, and `BRANCH_NAME`.
This means next time you run `gitf` these options must not be included in your command
Below is the command that must be used.
```bash
gitf -t [GITHUB_PERSONAL_TOKEN] -m "[message_to_attach to changes made]"
```
### HINT
You can use one folder only for all repositories you need to modify this way. All you need is to create different branches and
give them names similar to the repositories they correspond to.

### PLANS
The project is still under development and expect more features to be included.
