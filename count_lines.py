#f=open('text1.txt', 'r')
#f.read 
#text=f.read()
marker = 0
f=open ('./text1.txt')
for line in f:
	marker +=1
	print (marker,line)
#print (text)
#print ('hello Polina ')
f.close
