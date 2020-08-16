# Quickly Project Start

### Install (Linux, Mac): 
```bash
git clone "https://github.com/FIMehedi/quickly-project-start.git" ~/.quickly-project-start
cd ~/.quickly-project-start
pip3 install -r requirements.txt
echo 'USER="Your Github Username"\nPASS="Your Github Password"\nTOKEN="Your Github Account token"' >> .env # Token optional
# Don't forget to use your own username and password.
echo 'source ~/.quickly-project-start/.project-commands.sh' >> ~/.bashrc # rc file edit
# If you're using zsh, replace ~/.bashrc to ~/.zshrc
source ~/.bashrc # For zsh source ~/.zshrc
```

### Install (Windows): 
> **_NOTE:_** You must use [Git Bash](https://git-scm.com/download/win)
```bash
git clone "https://github.com/FIMehedi/quickly-project-start.git" ~/.quickly-project-start
cd ~/.quickly-project-start
pip install -r requirements.txt
echo 'USER="Your Github Username"
PASS="Your Github Password"
TOKEN="Your Github Account token"' >> .env # Token optional
# Don't forget to use your own username and password.
echo 'source ~/.quickly-project-start/.project-commands-win.sh' >> ~/.bashrc
source ~/.bashrc
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
