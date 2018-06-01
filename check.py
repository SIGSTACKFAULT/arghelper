import discord, pycurl, sys
import try_url

from bases import bases

suffixes = [
	".png",
	".jpg",
	".gif"
]

def permutations(thing):
	# get 'em all, even if the base doesn't have a suffix:
	p = []
	for base in bases:
		for suffix in suffixes:
			# we need an immutable type for set(); we'll turn this into a dict later.
			p.append((base, base.format(thing=thing, suffix=suffix)))

	# remove dupes
	q = list(set(p))

	#now make it back into a list of dicts.
	r = {i[0]:i[1] for i in q}
	return r

async def try_and_send(client, M, thing, opts={}):
	await client.send_typing(M.channel)
	p = permutations(thing)
	out = []
	for base, permutation in p.items():
		code = try_url.try_url(permutation, opts=opts)
		if((code in bases[base]) or (opts.get("verbose", False) == True)):
			out.append("<{url}> - {code}".format(url=permutation, code=code))
	
	out.sort()
	if(out == []):
		await client.send_message(M.channel, "`{thing}`: None found.".format(thing=thing))
	else:
		await client.send_message(M.channel, "\n".join(out))


def parse_flags(argv):
	opts = {
		"nocache" : False,
		"verbose" : False
	}
	opt_map = {
		"nocache" : {
			True : ["-c", "--nocache"],
			False: ["-C", "--cache"]
		},
		"verbose" : {
			True : ["-v", "--verbose"],
			False: []
		}
	}
	for option, triggers in opt_map.items():
		for trigger, flags in triggers.items():
			for flag in flags:
				for i, arg in enumerate(argv):
					if(arg == flag):
						opts[option] = trigger
						argv.pop(i)
				
	return opts, argv
	

async def check(client, M, argv):
	"""The actual function called by main"""
	opts, argv = parse_flags(argv)
	ulist = argv[1:]
	if(ulist == []):
		await client.send_message(M.channel, "?")
	else:
		for url in ulist:
			await try_and_send(client, M, url, opts=opts)

async def getUserAgent(client, M, argv):
	await client.send_message(M.channel, "```\n"+client.curl_agent+"\n```")


# Unit test.
if(__name__ == "__main__"):
	if("-v" in sys.argv):
		curl_verb = True
	else:
		curl_verb = False
	code = try_url("https://tinyimg.io/i/HlKgkKP.png", curl_verb=curl_verb)
	print(code)
