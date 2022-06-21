lcl="abcdefghijklmnopqrstuvwxyz"
ucl="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
l=lcl+ucl
d="0123456789"
a=input()
l_n=0
d_n=0
for i in a:
	if(i in l):l_n+=1
	if(i in d):d_n+=1
print("LETTERS",l_n)
print("DIGITS",d_n)
