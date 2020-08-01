first = 2
last = 10000
file = open("prime.txt","w")

for i in range(first, last+1):
	for j in range(2, i):
		if (i % j) == 0:
			break
	else:
		# print(i)
		file.write(str(i)+"\n")
			
file.close()