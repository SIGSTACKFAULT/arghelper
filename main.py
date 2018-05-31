#!/usr/bin/python3
import discord, json, pycurl
import check, cache


VERSION="0.1"
PREFIX="%"
USERAGENT = "sbhelperbot/{bot_version} ({pycurl_version})".format(
	bot_version=VERSION,
	pycurl_version=pycurl.version
)

with open("token", "r") as f:
	TOKEN = f.read().rstrip()


client = discord.Client()

client.bot_version = VERSION
client.bot_prefix = PREFIX
client.curl_agent = USERAGENT

cmds = {
	"check"	: check.check,
	"useragent" : check.getUserAgent,
	"getcache" : cache.getcache
}

@client.event
async def on_ready():
	print("Connected!")
	print("----------\n")

@client.event
async def on_message(M):
	for key, value in cmds.items():
		if(M.content.startswith(PREFIX + key)):
			argv = M.content.split()
			await value(client, M, argv)
			return
		

client.run(TOKEN)
