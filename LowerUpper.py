lcl="abcdefghijklmnopqrstuvwxyz"
ucl="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a=input()
l_n=0
u_n=0
for i in a:
	if(i in lcl):l_n+=1
	if(i in ucl):u_n+=1
print("UPPER CASE",u_n)
print("LOWER CASE",l_n)
