Title: Adjusting Screen Brightness on Ubuntu 12.04
Published: 28-06-2012
Tags: Linux, Ubuntu

Since Ubuntu 11.x I have not been able to adjust the screen brightness of my
Samsung Laptop. The default brightness is close to the maximum value.

I wanted to take a jab at solving this issue by using the collective
intelligence of the internets :) and came across a couple of solutions in the
Ubuntu forum. One of them worked for my case.

<more/>

All I had to do was edit my xorg.conf file and add the following settings

    Option "RegistryDwords" "EnableBrightnessControl=1"

After adding the above directive the conf should look like this:

![Conf](/static/d3d86-43-scaled1000.png)

Once the above directive is added restart the system and the brightness
adjustment should work fine. To read about the other solutions provided in the
thread visit
[http://ubuntuforums.org/showthread.php?t=1875126](http://ubuntuforums.org/showthread.php?t=1875126)

Update: I also came across another blog entry which had solved the issue for
some folks. You can find the entry here
[http://elleestcrimi.me/2011/11/06/quick-tip-3-fix-screen-brightness-issue-samsung-netbooks-running-ubuntu/](http://elleestcrimi.me/2011/11/06/quick-tip-3-fix-screen-brightness-issue-samsung-netbooks-running-ubuntu/)
