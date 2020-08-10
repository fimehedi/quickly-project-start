from dotenv import load_dotenv
from github import Github
from os import getenv, system
from sys import argv


load_dotenv()
github_user  = getenv("USER")
github_pass  = getenv("PASS")
github_token = getenv("TOKEN")

try:
    project_name = argv[1]
except:
    print("Command Not Found!")


def local_project_remove():
    system("rm -rf " + project_name)


def github_repo_remove():
    github_user_login = Github(github_user, github_pass).get_user() # Login by username and password
    #github_user_login = Github(github_token).get_user() # Login by token
    repo = github_user_login.get_repo(project_name)
    repo.delete()


if __name__ == "__main__":
    try:
        if argv[2] == '-':
            confirm = input("Deletion (2)\n1. {} (Local)\n2. {} (Github)\nAre you sure?[y/n] : ".format(project_name, project_name))
            if confirm.lower() == 'y':
                local_project_remove()
                github_repo_remove()
                print("Deletion (2) Success!")
        elif argv[2] == '--l':
            confirm = input("Deletion (1)\n1. {} (Local)\nAre you sure?[y/n] : ".format(project_name))
            if confirm.lower() == 'y':
                local_project_remove()
                print("Deletion (1) Success!")
        elif argv[2] == '--r':
            confirm = input("Deletion (1)\n1. {} (Github)\nAre you sure?[y/n] : ".format(project_name))
            if confirm.lower() == 'y':
                github_repo_remove()
                print("Deletion (1) Success!")
        else:
            print("Command Not Found!")

    except Exception as e:
        print(e)