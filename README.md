# arghelper
Discord bot to help with generic ARG solving.

## Synopsis

<pre>
check [-v] <em>query</em>...
</pre>

## Description

Sends url requests to multiple file hosting services.
Current available services:
* Imgur.com
* tinyimg.io
* cubeupload.com
* youtube.com

Also tries suffixes, where applicable:

* .png
* .jpg

Naturally, it won't try anything like `https://youtube.com/watch?v=dQw4w9WgXcQ.png`
