# get the size of the repo 


#You could use GitPython library, for instance:

import re
import git

repo_path = '.'
repo = git.Repo(repo_path)
git = repo.git

git.gc()
res = git.count_objects('-vH')

print(re.search(r'size: .*', res).group())
# 'size: 376.00 KiB'
#To understand why this method of finding the size of a repo is preferable, check out this discussion: Find size of git repo
