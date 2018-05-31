# arghelper
Discord bot to help with generic ARG solving.

## Synopsis

<pre>
%check [-v] <em>query</em>...
</pre>

The prefix (default `%`) is configurable in `main.py`.

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

## Fast

It's *blisteringly* fast. It uses PycURL, which is itself a thin wrapper around cURL, probably the fastest HTTP library out there.
It only does http HEAD reqests, so it doesn't waste any time downloading the actual image body or (more likley) the 404 page.

## Configurable

Adding new schemes is easy. There's an array at the top of `check.py`. It's also possible to specify which HTTP codes mean found, if you needed that for some reason.
