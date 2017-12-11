list=[]

def fib(n):
    if n==0:
        return 0
	if n==1:
		return 1
    else:
        return (fib(n-1)+fib(n-2)) 

		
n = int (input("masukkan banyak bilangan fibnacci :")) 
#print(fib(n))
for i in range (n): 
	list.append(fib(i)) 

print(list)