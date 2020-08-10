from os import getenv, system
from sys import argv
from webbrowser import open_new_tab

try:
    project_name = argv[1]
except:
    print("Command Not Found!")


def project_open_with_editor():
    system("code " + project_name)


def github_repo_open_with_browser():
    user = getenv("USER")
    open_new_tab("https://github.com/{}/{}".format(user, project_name))


if __name__ == "__main__":
    try:
        if argv[2] == '-':
            project_open_with_editor()
            github_repo_open_with_browser()
        elif argv[2] == '--l':
            project_open_with_editor()
        elif argv[2] == '--r':
            github_repo_open_with_browser()
        else:
            print("Command Not Found!")

    except Exception as e:
        print(e)