Title: git submodule update !fail!
Published: 18-05-2014
Tags: git, Tech Recipes
Visibility: public

I usually find git error messages helpful and this time it was no
exception. While updating submodules after a checking out a repo
the following error output was spewed out to [CLI][c].

    [someuser@remotehost]$ git submodule update
    Cloning into somerepo...
    Permission denied (publickey).
    fatal: The remote end hung up unexpectedly
    Clone of 'git@github.com:somerepo/somerepo-somerepo.git' into submodule path

The second line of the output indicates the issue. git was trying to use key
based authentication via [SSH][s]. Well it's quite straight forward (or so I
thought) as all I have to do is change the URL to web [URL][u] and I should be
able to update the submodule.  I opened up `.git/config` made the necessary
changes and tried to update the submodule to no avail. Tried doing the same thing by
recloning the repo again and yet no luck.

Googling around a bit I came across this SO post
[http://stackoverflow.com/questions/8197089/fatal-error-when-updating-submodule-using-git][so]
which was the exact problem I was facing and the last answer nailed it!

###Solution

Apparently the answer lies in updating 3 files instead of only `.git/config.`
The files are:

* `.gitsubmodules`
* `.git/config`
* `.git/modules/example/config`

And therefter run the following commands

    git submodule sync
    git submodule init
    git submodule update

The solution in itself is simple and one can't help but feel a bit stupid.
However, the reason I least expected this chain of alterations was that I did
not expect such duplications in a high quality utility such as git. Initially I
was suprised and disappointed at the same time but to reason this duplication
might prove to be interesting and perhaps would result in another short post :).

[c]: http://en.wikipedia.org/wiki/Command-line_interface
[s]: http://en.wikipedia.org/wiki/Secure_Shell
[u]: http://en.wikipedia.org/wiki/Uniform_resource_locator
[so]: http://stackoverflow.com/questions/8197089/fatal-error-when-updating-submodule-using-git
