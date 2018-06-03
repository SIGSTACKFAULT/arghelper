import pycurl
WHOAMI="arghelper"
URL="https://github.com/Blacksilver42/arghelper"
VERSION="1.0.0"
VERSIONSTRING="BugFree(tm)"
PREFIX="%"
USERAGENT = "{whoami}/{bot_version} ({pycurl_version})".format(
	whoami=WHOAMI,
	bot_version=VERSION,
	pycurl_version=pycurl.version
)
CACHEFILE = "cache.json"
ZIP_CACHE = True
ZIP_CACHEFILE = "cache.z"
