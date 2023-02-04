def fac(n):
	if n==1:
	  return n
	else:
	  return n*fac(n-1)

num=int(input("Enter the number :"))
print(fac(num))