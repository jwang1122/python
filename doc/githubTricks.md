<h1>GitHub Tricks</h1>

## delete a repository
1. open the repository
2. ⚙️ Settings
3. scroll down all the way to the buttom
4. click [Delete this repository]

## rename a repository
1. open the repository
2. ⚙️ Settings
3. change name

.git/config

```
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://github.com/jwang1122/python.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
[user]
	name = jwang1122
	email = jwang1122@gmail.com
```