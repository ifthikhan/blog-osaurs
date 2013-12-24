Title: Tee
Published: 20-01-2013
Tags: Linux, CLI, Tech-recipe

I have come across "TEE" few times but never found a compelling reason to use.
Sure I have heard about parallelizing operations when working with large files
but never came up with a use-case specific to my situation until today.

<more/>

I was configuring the iptables rules of a Linux server and encountered the
following when try to save:

    $ sudo iptables-save > /etc/iptables.up.rules

Executing the above command I was greeted with:

    -bash: /etc/iptables.up.rules: Permission denied

At first glance the error message seemed a bit dubious, however if you fixate
on it a little longer and your expression would change to "aha" gotcha. The way
the user privileges is intepreted with such a command is > root > currently
running user and hence the redirection operator cannot write to the file
system. You can  either run the entire command on a subshell with root
priviledges like below

    $ sudo sh -c "iptables-save > /etc/iptables.rules"

or tee the standard input to the file. This command will write the output to
STDOUT and to the file.

    $ sudo iptables-save | sudo tee /etc/iptables.up.rules

An illustration of "TEE" from
[Wikipedia](http://en.wikipedia.org/wiki/Tee_%28command%29)

![Tee](/static/0d87b-tee-svg-scaled1000.jpg)
