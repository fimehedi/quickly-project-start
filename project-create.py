from dotenv import load_dotenv
from github import Github
from os import getenv, system, chdir
from sys import argv


load_dotenv()
github_user  = getenv("USER")
github_pass  = getenv("PASS")
github_token = getenv("TOKEN")

try:
    project_name = str(argv[1])
except:
    print("Commnad Not Found!")


def local_repo_create():
    all_command = [
        "git init",
        "touch .gitignore",
        "git add .gitignore",
        "git commit -m 'Initial Commit'",
        # IF you are using HTTPS
        "git remote add origin https://github.com/{}/{}.git".format(github_user, project_name),
        #IF you are using SSH
        # "git remote add origin git@github.com:{}/{}.git".format(github_user, project_name),
        "git push -u origin master",
        "code ."
        ]
    for command in all_command:
        system(command)


def github_repo_create():
    github_user_login = Github(github_user, github_pass).get_user() # Login by username and password
    #github_user_login = Github(github_token).get_user() # Login by token
    repo = github_user_login.create_repo(project_name)


if __name__ == "__main__":
    try:
        if argv[2] == '-':
            local_repo_create()
            github_repo_create()
            print("Creation (2)\n1. {} (Local)\n2. {} (Github)".format(project_name, project_name))
        elif argv[2] == '--l':
            local_repo_create()
            print("Creation (1)\n1. {} (Local)".format(project_name))
        elif argv[2] == '--r':
            github_repo_create()
            print("Creation (1)\n1. {} (Github)".format(project_name))
        else:
            print("Command Not Found!")

    except Exception as e:
        print(e)




