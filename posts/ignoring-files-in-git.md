Title: Ignoring files in git
Published: 26-12-2013
Tags: Git
Visibility: public

Ignoring files in git is very simple, add the pattern to a ".gitignore" file.
Everytime I create a new repo I have to go through the motion of creating a new
ignore file and add the types of files to be ignored.

As I was going through these motions today I decided to investigate if git has an
option to globally ignore files across local repositories. The results I saw were quite
amazing. It has more options than I thought and fits all my use cases
perfectly (beautiful by design). I have listed each of the options below:

* .gitignore
* Globally ignoring files
* Local repository exclude
* Ignore versioned files

###.gitignore
Good ole `.gitignore` file we are all familiar with. This file is
available for every repo and is committed and **shared by everyone** cloning the
repo. This is useful for common files or directories created by the project
which should not be versioned.

###Global git ignore
A global git exclude file can be created to ignore files
across all locally cloned repositories. This is a system wide file. Create a
file eg: `~/.gitignore_global` (the name is irrelevent) and then indicate it
to git by running the command
`git config --global core.excludesfile ~/.gitignore_global`. This is
extremely handy to avoid duplicating the same ignore directives across all
local repositories.

###Local repository exclude
This feature is used when you have to ignore
directives which are relevant to your local environment. For an instance
files or directories created by your IDE or other utilities such as ctags.
This is acheived by editing the repos `.git/info/exclude` file

###Ignore versioned files
There are versioned files in most local repos
which are edited but not committed. For an instance certain config values
needs to be altered for each developer's local environment. While these files
cannot be ignored but keeping them in a dirty state is a hassle as it
requires multiple dances between `git stash` and `git pop`. Git offers the
following command `git update-index --assume-unchanged path/to/file`. In case
you want to commit certain changes to these files you can run the following
command `git update-index --no-assume-unchanged path/to/file`.

There are couple of gotchas related to this command:

- In case someone made a change to a file ingored with this feature and you
  pull the new changes, git will report that it's unable to merge the new
  changeset as there are uncomitted changes in the ignored file. If you do
  a `git status` nothing will be reported as the file is ignored locally.
  You have to unignore (for the lack of a better term :)), perform the pull
  and ignore it again.

- Performing a `git reset --hard` will revert the files ignored using this
  mechanism.
