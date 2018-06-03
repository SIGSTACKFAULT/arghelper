import pycurl, zlib

WHOAMI="arghelper"
VERSION="0.3.1"
VERSIONSTRING="The Zipper"
PREFIX="%"
USERAGENT = "{whoami}/{bot_version} ({pycurl_version})".format(
	whoami=WHOAMI,
	bot_version=VERSION,
	pycurl_version=pycurl.version
)
CACHEFILE = "cache.json"
ZIP_CACHE = True
ZIP_CACHEFILE = "cache.z"

def discord_version():
	return """**{whoami}:** {bot_version} *\"{versionstring}\"*
**pycurl:** {pycurl_version}
**zlib:** {zlib_version}""".format(
	whoami=WHOAMI,
	bot_version=VERSION,
	versionstring=VERSIONSTRING,
	pycurl_version=pycurl.version_info()[1],
	zlib_version=zlib.ZLIB_VERSION
)

async def getUserAgent(client, M, argv):
	await client.send_message(M.channel, "```\n{}```\n".format(USERAGENT))
async def getVersion(client, M, argv):
	await client.send_message(M.channel, discord_version())

if(__name__ == "__main__"):
	print(human_version())
