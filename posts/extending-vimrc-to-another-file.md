Title: Extending vimrc to another file
Published: 31-01-2014
Tags: Vim
Visibility: private

My vimrc is hosted on github and I pull it on the multiple environments that I
work on. These environments include home laptop, the desktop at work and
within the cloud instances where I perform a large portion of my work. In some
of these environments minor changes to the setting is required and keeping
multiple versions of the file is a headache and further altering after pulling
and then stashing the rc on each  pull or prior to making changes for push is a
headache. To get rid of this hassle I wanted to create another file where I
could add these additional host specific configurations

It turns out that there vim will only read one vimrc file and stop the search.
I started hacking out a few snippets in the rc file. The idea is quite simple
check for the existence of a particular file and if available source it.

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
