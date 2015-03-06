Title: Tales of a Shell Ninja - XARGS
Published: 06-02-2015
Tags: CLI

Every once in a while I discover nifty features of shell and have been itching to share :). Here goes the first in a serieis of **shell** tales.

[XARGS][x] is usually used when the output of a command which is `\n` seperated needs to be the input of another command. Passing the command the and piped input to `xarg` it builds the input and pass it to the given command.

    $ seq 10 | xargs echo ">>"
    >> 1 2 3 4 5 6 7 8 9 10-

Note: The output of `seq` was passed in one batch to `echo`

In addition to the above another very useful feature (the best IMO) it offers is the ability to run a single command with multiple arguments in parallel

    $ seq 10 | xargs -P 10 -n 1 echo ">>"
    >> 1
    >> 3
    >> 2
    >> 4
    >> 5
    >> 6
    >> 7
    >> 8
    >> 9
    >> 10

Note: The numbers are **NOT** printed in order. Each line of output 

* `-P` Indicate the number of processes 
* `-n` Specifies the number of arguments from piped input to pass to single execution of the command.

[x]: http://en.wikipedia.org/wiki/Xargs

Read this article for further ideas http://offbytwo.com/2011/06/26/things-you-didnt-know-about-xargs.html.

Happy shelling ;) (Not literally!)
