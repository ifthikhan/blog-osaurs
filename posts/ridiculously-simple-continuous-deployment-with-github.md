Title: Ridiculously Simple Continuous Deployment with Github
Published: 29-12-2013
Tags: Git, Linux
Visibility: public

Yep you heard it right, it's extremely simple!

Recently I migrated my blog from wordpress to a custom made simple blogging
engine. It's powered by [flask](http://flask.pocoo.org/) and the posts are written in
[markdown](http://en.wikipedia.org/wiki/Markdown). Once it was done I sighed a
breath of relief, finally, far, far away from the clutter of popular blogging platforms.

Although using markdown and flask was simple and easy, this approach incured
an extra step of deploying the changes to the server. A typical workflow was:
write, push the changeset to github, login into my server and pull the
changes. For a given post this might have to be done a few times and code
changes have to be deployed the same. Automation was screaming at the top of
it's voice and I new things had to change if my new found love was to sustain.

<more/>

###Git Web Hooks
Going through github I came across [git web
hooks](https://help.github.com/articles/post-receive-hooks). This allows you to
specify a url and when a changeset is pushed the given url will be invoked.

### Good Ole' CGI, Shell Script and Apache
Adding an HTTP endpoint to the blogging application is more complicated since
the webserver will not have write permissions and mixing deployment concerns
within the application is UGLY by design.

Alternatively I decided to make use of the good ole' cgi-bin and add a shell
script which will su to the owner of the application directory and run `git
pull` to update the application.

###Security, security.... security
Allowing apache to run as another user is quite dangerous but using sudo it
can be restricted to run as only the given user and only a given command, see
the following code samples to see how it's done.

Shell script to perform git pull

    #!/bin/bash
    pushd /path/to/the/application/directory
    unset GIT_DIR
    sudo -u <web directory owner> git pull # Switches as another user
    popd

Setting permissions in sudo to allow apache `www-data` to switch to the web directory owner and execute only git pull

    www-data myhost=(web-directory-owner)NOPASSWD:/usr/bin/git pull

- www-data: Apache user.
- myhost: The name of the host to ensure this cannot be done remotely.
- web-directory-owner: The user to be switched into.
- NOPASSWD: Do not prompt for password.
- /usr/bin/git pull: Only the git pull command can be executed.

The following apache directives can be added to the virtual host:

    ScriptAlias /cgi-bin/ "/var/www/blogosaurs/cgi-bin/"
    <Directory "/var/www/html/cgi-bin">
            Options +ExecCGI
            AddHandler cgi-script .cgi
    </Directory>

The above set-up works beautifully. Every time I push a changeset to github, it's automatically deployed to the server and changes are instantly live.

![CD](/static/got-continuous-deployment.jpg)

Happy coding :)
