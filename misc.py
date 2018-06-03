import discord, settings

def embed_version():
	em = discord.Embed(
		title="{i} {v} \"{vs}\"".format(i=settings.WHOAMI, v=settings.VERSION, vs=settings.VERSIONSTRING),
		url=URL
	)
	em.add_field(name="discord.py", value=discord.__version__)
	em.add_field(name="PycURL", value=pycurl.version_info()[1])
	em.add_field(name="zlib", value=zlib.ZLIB_VERSION)
	return em

async def getUserAgent(client, M, argv):
	await client.send_message(M.channel, "```\n{}```\n".format(settings.USERAGENT))
async def getVersion(client, M, argv):
	await client.send_message(M.channel, embed=embed_version())


