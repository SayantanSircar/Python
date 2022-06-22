
a=input()
str1=a.split()
uniq=[]
for i in str1:
	if i not in uniq:
		uniq.append(i)
sort(uniq)
for i in range(0,len(uniq)):
	print(uniq[i],str1.count(uniq[i]))