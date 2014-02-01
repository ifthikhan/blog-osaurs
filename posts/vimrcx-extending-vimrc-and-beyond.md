Title: VimrcX, extending Vimrc
Published: 31-01-2014
Tags: Vim
Visibility: public

Being a Vim addict, one develops a natural tendency to spend countless hours
taming it to one's own needs and desires. A manifestation of this effort is my
vimrc on Github.

###Vim everywhere
I work on multiple hosts every day. My laptop at home, laptop at work,
desktop at work as well the virtual machine where most of the actual development
takes place. All these instances have my vimrc and moving from one to the other
is a seamless experience!

###Customization craze
However, it turns out that for the ultimate annoyance free editing (if there is
such a thing ;)) each of these environments' demands it's own tweak. Special
dirs to be excluded so that wild menu, ctrlp or ack does not display these
unwanted options, indentation settings etc...

###VimrcX
Since each host requires it's own special tweak a plugin will not work. I
decided to try extending vimrc to another file. As Vim stops searching
for a config once it encounters the first one the only option I had was to
to source another file inside the current one.

The snippet below looks for a file named `.vimrcx` in the user's home dir and if
it exists sources the file.

    function! GetHomeDir()
        return system('echo -n $HOME')
    endfunction

    " Add a file named ~/.vimrcx in the home directory to override vimrc
    " settings specific to the current host
    let g:if_extended_vimrc = GetHomeDir() . '/.vimrcx'
    if filereadable(g:if_extended_vimrc)
        so `=g:if_extended_vimrc`
    endif


Although the above snippet is quite simple I discovered a couple of nifty
features in Vim to pull it off.

- *system('echo -n $HOME'):* The system function executes a shell command and
  returns the output so it can be stored in a variable.
- *so `=g:if_extended_vimrc`:* Using backticks to expand vim expressions. When
  an expression is enclosed in backticks with an `=` at the beginning the
  expression is treated as a vim expression.

###Usage
With the above feature in place, I decided to set-up conditionally toggling
stripping of trailing whitespace characters for a given host.

The following is in my vimrc:

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

I add the below snippet to `.vimrx` and enable the feature.

    g:ifrc_strip_trail_spaces

With `.vimrcx` in place any of the vim options can be set, unset or altered to
suite the environment I am working on.

Happy hacking :)
