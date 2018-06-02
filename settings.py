import pycurl

WHOAMI="arghelper"
VERSION="0.2.1"
PREFIX="%"
USERAGENT = "{whoami}/{bot_version} ({pycurl_version})".format(
	whoami=WHOAMI,
	bot_version=VERSION,
	pycurl_version=pycurl.version
)

def human_version():
	return "**{whoami}:** {bot_version}\n**pycurl:** {pycurl_version}".format(
	whoami=WHOAMI,
	bot_version=VERSION,
	pycurl_version=pycurl.version_info()[1]
)
	

if(__name__ == "__main__"):
	print(human_version())
