b=[]
a=input()
while(a):
    b.append(a)
    a=input()
w,x,y,z=[],[],[],[]
for i in b:
	if(i[0:2]=="UP"):w.append(int(i[3:]))
	if(i[0:4]=="DOWN"):x.append(int(i[5:]))
	if(i[0:4]=="LEFT"):y.append(int(i[5:]))
	if(i[0:5]=="RIGHT"):z.append(int(i[6:]))
g,h=sum(w)-sum(x),sum(y)-sum(z)
p=[]
p.append(abs(g))
p.append(abs(h))
print(max(p))