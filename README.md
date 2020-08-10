# Quick Project Create
---
**NOTE**

This project is only for Linux and Mac users. For windows version you need to wait some couple of time

---

### Install (Linux & Mac): 
```bash
git clone "https://github.com/FIMehedi/quickly-project-start.git" ~/.quick-project-create
cd ~/.quick-project-create
pip3 install -r requirements.txt
mv default.env .env
# Then open .env file and update by your github username password or token (if you want to login github by token). Don't change file format.
source ~/.quick-project-create/.project-commands.sh
vim ~/.bashrc # then insert 'source ~/.quick-project-create/.project-commands.sh' for zsh it will be vim ~/.zshrc
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
