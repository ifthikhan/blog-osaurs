Title: Fetching FLV URL of a YouTube video in PHP
Published: 14-04-2011
Tags: PHP, YouTube

Recently I came across a requirement to fetch few details for a given YouTube
video URL. The details were Title, Description and the URL of the FLV video
stream. Details such as Title and Description can be retreived by using a
library such as Zend_Gdata_YouTube. However finding out the url of the FLV
stream is tricky.

<more/>

Googling for "getting flv url from youtube" brought me some results, almost all
of them were outdated. I had no choice but to roll-up my sleeves and figure it
out by myself.

Using a web proxy debugger I was able to trace the http call made by the player
to fetch the details of the video. The URL for this call is

    http://youtube.com/get_video_info?video_id=<id of the video>.

A request to the above url with a video id suffixed will bring a whole host of
details regarding the video. The data sent back by the server is in the form of
a query string (key/value pairs seperated by an "&"). Details include title,
rating, url to the thumbnail, a map of urls to flv for different resolutions
and much more.

    &fmt_url_map=37|http://v16.lscache4.c.youtube.com/videoplayback?sparams=id%2Cexpire%2Cip%2Cipbits%2Citag%2Cratebypass%2Coc%3AU0hPRlhOV19FSkNOOV9QSEFD&itag=37&ipbits=0&signature=CA388187960DBCF8362F8D99E79B50143A77CE69.7B33563537A1B31B86F3617169C2550FD3FB2940&sver=3&ratebypass=yes&expire=1301839200&key=yt1&ip=0.0.0.0&id=09ff90c6ce84e4e9,22
    |http://v2.lscache8.c.youtube.com/videoplayback?sparams=id%2Cexpire%2Cip%2Cipbits%2Citag%2Cratebypass%2Coc%3AU0hPRlhOV19FSkNOOV9QSEFD&itag=22&ipbits=0&signature=362B43A5AE2AC594C878470BDD809D77CC5DBAEF.243AADA0B9ED19070C9C721A2CBA9C8520F87122&sver=3&ratebypass=yes&expire=1301839200&key=yt1&ip=0.0.0.0&id=09ff90c6ce84e4e9,35
    .....
    ...
    &allow_ratings=0

The URLs' are seperated by "|", and further each url is suffixed by a "," and a
number. A while back YouTube started offering videos to be viewed in various
resolutions. The number after the comma is the quality value. Wikipedia has a
table of these numbers and the resolutions.

My initial thought was to explode the response string by "&" and query the
values for any given key. This is not possible since the values themselves have
urls with query strings and exploding by "&" will not yield the required
results. This baffled me as there have to be someway the player is able to put
this string into a data structure and query the required values from it. I
thought for a while but could not come up with anything apart from regex
pattern matching.

I wrapped the necessary call to fetch the data from the above url and to obtain
the url to the flv's in a class called YouTube_VideoInfo. Feel free to download
it and use it for your projects or requirements. You can download the code from
here
