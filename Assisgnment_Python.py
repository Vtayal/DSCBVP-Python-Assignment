#Question 1
l=[]
for i in range(2000,3201):
	if(i%7==0) and (i%5!=0):
		l.append(i)
print("Nos. divisible by 7 and not 5-->",l,'\n')


#Question 2
d={}
n=int(input("Enter a number-->"))
for i in range(n):
	d[i+1]=(i+1)**2
print(d,'\n')


#Question 3
n=int(input("Enter a number to find its Factorial-->"))
x=1
if(n==0):
	print("x")
else:
	for i in range(n,1,-1):
		x*=i
print("Factorial of",n,"-->",x,'\n')


#Question 4
a=[5,7,9,3,2,1,4,2,6,3,0,9,8]
print("a-->",a)
b=[]
c=0
for i in a:
	if(i<5):
		b.append(i)
print("List of numbers <5-->",b)
n=int(input("Enter a number to check it in list a-->"))
for i in range(len(a)):
	if(a[i]==n):
		print("number found at position",i+1,'\n')
		c+=1
		break
if(c==0):
	print("\"Number not found\"",'\n')


#Question 5
word=str(input("Enter a short sentence-->"))
word=word.upper()
print(word,'\n')


#Question 6
n=int(input("Enter a number-->"))
l=[]
binary=""
while (n>0):
	l.append(n%2)
	n//=2
for i in range(len(l)):
	binary+=str(l.pop())
print("Binary form-->",binary,'\n')


#Question 7
word=str(input("Enter a short sentence-->"))
words=word.split()
ans=""
for i in range(len(words)):
	ans+=words.pop()+" "
print("Reversed string-->",ans,'\n')


#Question 8
n=1
for i in range(1,5):
	for j in range(i,i+n):
		print(j,end="")
	print("")
	n+=1
print('\n')


#Question 9
class Circle:
	def __init__(self,radius):
		self.radius=radius
	def area(self,pi):
		return(pi*self.radius*self.radius)
pi=float(22/7)		
n=int(input("Enter radius of circle-->"))
circle=Circle(n)
print("Area-->",circle.area(pi),'\n')


#Question 10
class string:
	def __init__(self):
		self.word=""

	def getstring(self):
		self.word=str(input("Enter a short sentence-->"))

	def printstring(self):
		self.word=self.word.upper()
		print("In upper case-->",self.word,'\n')

obj=string()
obj.getstring()
obj.printstring()


#Question 11
word=str(input("Enter a short sentence-->"))
word=word.split()
d={}
for i in word:
	a=0
	for j in word:
		if(i==j):
			a+=1
	d[i]=a
for key in sorted(d):
    print (key,":",d[key])