def istrcmp(a,b):
	c,d=a.lower(),b.lower()
	if d in c:
		return True
	else:
		return False

a="xyz is my name"
b="my name"
x=istrcmp(a,b)
print(x)