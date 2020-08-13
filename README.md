# Quickly Project Start

### Install (Linux, Mac & Windows): 
> **_NOTE:_** If you're a Windows user, you must use [Git Bash](https://git-scm.com/download/win)
```bash
git clone "https://github.com/FIMehedi/quickly-project-start.git" ~/.quick-project-create
cd ~/.quick-project-create
pip3 install -r requirements.txt
mv default.env .env
# Then open .env file and update by your github username password or token (if you want to login github by token). Don't change file format.
echo 'source ~/.quick-project-create/.project-commands.sh' >> ~/.bashrc # rc file edit
# If you're using zsh, replace ~/.bashrc to ~/.zshrc
source ~/.bashrc # For zsh source ~/.zshrc
```

### Usage:
```bash
project-{command} <project-name> {option (optional)}
```

#### Commands:
```
create : For create a new project (Local and github) and open with Editor
open   : For open exsist project with Editor
remove : For remove exsist project (Local and github)
```	

#### Options:
```
-l  : Command only for local
-r  : Command only for remote
```
