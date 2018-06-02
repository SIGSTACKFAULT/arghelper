import pycurl

VERSION="0.2.0"
PREFIX="%"
USERAGENT = "sbhelper/{bot_version} ({pycurl_version})".format(
	bot_version=VERSION,
	pycurl_version=pycurl.version
)

if(__name__ == "__main__"):
	print("VERSION:  ", VERSION)
	print("PREFIX:   ", PREFIX)
	print("USERAGENT:", USERAGENT)
