import git

repo = git.Repo(r'F:\arbeit file\fypy\fypyup')

repo.remotes.origin.pull()