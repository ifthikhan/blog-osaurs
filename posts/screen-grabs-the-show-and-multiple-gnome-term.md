Title: Screen grabs the show and multiple gnome terminal tabs out...
Published: 1-05-2012
Tags: Linux, CLI

Lately I have been  doing loads of stuff, sadly I did not find the time nor the
motivation to write about them.

In order to break the ice I wanted to write-up on one of the tools which I have
been using lately and am pretty excited about "GNU Screen".

<more/>

Previously whenever I wanted to multi-task on the command line: login to a
remote server, edit code (VIM), monitor logs, perform adhoc tasks etc... (sounds
familiar), I used to open multiple Gnome Terminal tabs and used to shift
between them.This approach is clumsy and inefficient:

- Mult-tasking effectively in the CLI requires the user to keep an eye on all of
these tasks at the same time.

- Switching between the tabs either required the usage of mouse or linearly shift
from the current to the destination tab.

- Does not allow the user to make use of the wide screen used by dy devs these
days. A different utility such as "Terminator" is required if you want to split
the window into multiple regions.

- Using the same session from another computer or share it with another user is
  simply impossible.

And to say the least it beats my idea of going completely command-line :). I am
not sure whether to term this as tool smell (for the lack of a better word) but
it definitely seems like the wrong tool for the write job.

###Screen to the rescue

I was aware of screen for a while but did not have the opportunity to check it
out. Once I dived into it a few weeks back, it was love at first sight.

- I could have multiple windows,

- Name those windows,

- Switch between them in an easy and intuitive manner,

- Split the main terminal into multiple regions and open the various sessions
in each region

- With a few tweaks to screenrc added a status bar and a default start-up
set-up so that whenever a new screen session is created the workspace will be
nicely laid out as per my preferences.

![Screen](/static/627b8-screenshot-2-scaled1000.png)

All of this only took an hour or so to get-up and running. Thereafter worked
with it a bit more to get affiliated to the commands and keyboard shortcuts and
I was ready to go.
