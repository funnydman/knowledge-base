## Problem
> When trying to use git to connect via ssh, it tries to use the first one which is configured.

1) 
```bash 
eval `ssh-agent -s`
ssh-add ~/.ssh/key
```

2) 
```bash
GIT_SSH_COMMAND="ssh -i ~/.ssh/key" git push
```

3) 
content ~/.ssh/config

Host github.com
HostName github.com
IdentityFile /path/to/your/personal/github/private/key
User dandv

Host github-work
HostName github.com
IdentityFile /path/to/your/work/github/private/key
User workuser

Then, to clone a project as your personal user, just run the regular git clone command.

To clone the repo as the workuser, run `git clone git@github-work:company/project.git`


4) 
```bash
git config core.sshCommand 'ssh -i ~/.ssh/key' 
```
