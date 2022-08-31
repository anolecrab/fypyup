import git
import os

path = os.getcwd()
# print(path)
repo = git.Repo(path)

current = repo.head.commit

repo.remotes.origin.pull()

if current != repo.head.commit:
    print("It changed")
else:
    print("No changed")
# repo = git.Repo(r'F:\arbeit file\fypy\fypyup')
# repo.remotes.origin.pull()
