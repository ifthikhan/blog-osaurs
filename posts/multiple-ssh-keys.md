Title: Multiple SSH keys
Published: 21-01-2013
Tags: Linux, CLI, SSH

Lately I have become a huge fan of ssh passwordless logins. At work and at home
I have to login and out of multiple servers with different keys and therefore
needed an easy way to manage them.

Enter the world of SSH config and simplify your life :)

Assuming that you know nothing about working with ssh keys I will walk you
through the entire process.

1. Generate a pair of public private keys in your local machine.

        $ ssh-keygen -tr
        &gt; rsaGenerating public/private rsa key pair.Enter file in which to save the key (/home/mickey/.ssh/id_rsa):

    If this is the first key you are creating you could use the default path (by
    not specifying a path) or else for the sake of clarity you could suffix the
    filename to describe to which server the key belongs to (specify the full path
    to the file) eg: "/home/mickey/.ssh/id_rsa.localvm".

2. The above step will result in the creation of a couple of files. Assumming
that you did not specify a file path but used the default one, the following
files will be created in your ~/.ssh dir: id_rsa and id_rsa.pub. The latter is
the public key and needs to be stored in the remote server. In order to copy
the file to the remote server you could use the "scp" utility.

        $ scp id_rsa.pub username@remote_host:~/.ssh/

3. Now login to the remote host and inside .ssh directory perform the following

        $ cd .ssh$ cat id_rsa.pub > authorized_keys

    The second command creates an authorized_keys file and copies the contents of
    id_rsa.pub to the newly created file. The sshd server will look-up for public
    keys in this file.

4. Now from your local machine you would be able to login to the remote server
without passwords.

        $ ssh username@remote_host

Since logging-in in this manner is quite convenient, the hypothetical you ;)
decide to set-up passwordless entries to all your remote servers. You would
that there can only be one id_rsa file and the rest have to be named
differently. Also how can you specify to the ssh command which private key to
use for which server and if you have to specify a private key when logging-in
might as well use the password.

This is where SSH config comes to rescue. Nope, it's not a utility, it's a
simple text file which resides in the ".ssh" directory. It allows you to
specify the various properties for a given alias thus easing you the burden of
constant lookups and key strokes.

A typical ssh file looks like the following:

    Host vm    HostName samplesite.vm    IdentityFile ~/.ssh/id_rsa.vm    User ifthikhan

The phrase "vm" is an alias and the rest of the parameters are used by ssh
during authentication. If you execute

    $ ssh vm

It will use the appropriate private key, username and host to log-into the
remote host. You can also provide other options such as Port,
ServerALiveInterval etc...
