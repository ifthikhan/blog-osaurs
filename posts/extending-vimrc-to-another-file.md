Title: VimrcX: Vimrc and <em>BEYOND</em>
Published: 31-01-2014
Tags: Vim
Visibility: private

Usually vim users have their own vimrc file which they use it on all their development environments. I am no exception either, my .vimrc is hosted on Github and spend countless of hours tweaking it.

###Ubquity
I work on multiple hosts every day. I have my laptop at home, laptop at work, desktop at work as well the cloud instance where most of the actual development take place. All these instances have my vimrc and it makes developing in each of these environments a seamless experience.

###Customization craze
However it turns out that for the ultimate annoyance free editing each of these environment demands it's own tweak. It could be special dirs to be excluded so that wild menu, ctrlp or ack does not display these unwanted options, indentation settings, not stripping trailing whitespaces as it messes up commits with unwanted changes (real pain!) etc...

###VimrcX
Since each host requires it's own special tweak a plugin will not work. I decided to try extending vimrc to another file. Since vim will stop searching for a vimrc file the moment it finds the first one the only option I had was to find a way to source the vimrc extended file `.vimrcx` within the main vimrc file if it is present in the home directory. 

```
function! GetHomeDir()
    return system('echo -n $HOME')
    endfunction

" Add a file named ~/.vimrcx in the home directory to override vimrc settings
" specific to the current host
let g:if_extended_vimrc = GetHomeDir() . '/.vimrcx'
if filereadable(g:if_extended_vimrc)
    so `=g:if_extended_vimrc`
endif
```

Although the above snippet is quite simple I discovered a couple of nifty features to pull it off.

*  system('echo -n $HOME'): The system function executes a shell command and returns the output so it can be stored in a variable.
*


For example if I have the following snippet in my vimrc

```
function! StripTrailingSpaces()
    exe "normal ma"
    %s/\s\+$//e
    exe "normal `a"
endfunction

function! ThouShaltTryStrippingIt()
    if exists('g:ifrc_strip_trail_spaces') && g:ifrc_strip_trail_spaces == 1
        call StripTrailingSpaces()
    endif
endfunction

autocmd BufWritePre * call ThouShaltTryStrippingIt()
```

At home when working in my personal projects I maintain a strict policy of
cleaning up these sort of junk. However when working with code at work on
existing projects with tons of trailing spaces code reviewers sneer when they
see a changeset with unwanted changes (albeit they do long term good to remove
them).

In order for me to enable I have to declare and initialise the variable
`g:ifrc_strip_trail_spaces` to 1 in the extended rc file and trailing spaces
will be automatically stripped.

The code to source additional files into vimrc is quite easy.

```
" Returns the path of the home dir
function! GetHomeDir()
    return system('echo -n $HOME')
    endfunction

" Add a file named ~/.vimrcx in the home directory to override vimrc settings
" specific to the current host
let g:if_extended_vimrc = GetHomeDir() . '/.vimrcx'
if filereadable(g:if_extended_vimrc)
    so `=g:if_extended_vimrc`
endif
```

Few handy tricks to be noted here and shell command can be executed and the
return value can be store using the system function.

Also using backticks to expand vim expression instead of shell commands.
