Title: Shell Brace Expansion
Published: 27-10-2014
Tags: Linux, Shell
Visibility: public

Brace expansion allows to generate arbitrary strings in the shell. The coolest
part is that the filename(s) does not need to exist. The following examples should
give an idea on how to use it.

##Examples

Let's start by creating a few files.

    $ touch file{1,2,3}.txt
    $ ls
    file1.txt   file2.txt   file3.txt

Alternatively we could include the creation of a file with the name `file`
along with its siblings.

    $ touch file{,1,2,3}.txt
    $ ls
    file.txt    file1.txt   file2.txt   file3.txt

Copy a file.

    $ cp file{,0}.txt
    $ ls
    file.txt    file0.txt   file1.txt   file2.txt   file3.txt

<more/>
Move a file

    $ mv file{,master}.txt
    $ ls
    file0.txt   file1.txt   file2.txt   file3.txt filemaster.txt

A frequent use of brace expansion is when you want to perform any of the
abover operations on files which are deeply nested, the path
to the directory has to be typed only once:

    $ cp /opt/path/1/2/3/file1 /opt/path/1/2/3/file2

    to

    $ cp /opt/path/1/2/3/file{1,2}

Further to the above one could use brace expansion with other utilities such
compiling using gcc.

    $ gcc -o hello{,.c}

Multiple file uploads using scp

    $ scp file{1,2,3,4} remotehost:/uploads/
    
Grepping in multiple directories

    $ grep some-pattern /usr/{dir1, dir2}/

###References
* [http://www.gnu.org/software/bash/manual/bashref.html#Brace-Expansion](http://www.gnu.org/software/bash/manual/bashref.html#Brace-Expansion)
* [http://linux.byexamples.com/archives/30/smart-grouping-shorten-long-command-line/](http://linux.byexamples.com/archives/30/smart-grouping-shorten-long-command-line/)



Happy hacking :)
