def sum_list(x):
	sm = 0
	for y in x:
		sm = sm + y 
	return sm 
 

def prod_list(x):
	prod = 1
	for y in x:
		prod = prod * y
	return prod 

def rev_list(x):
	t = x
	t.reverse()
	return t 




def main():
	lst = []

	n = int(input("Enter number of elements :"))

	for i in range(0, n):
		ele = int(input())
		lst.append(ele)

	sm = sum_list(lst)
	pd = prod_list(lst)
	rv = rev_list(lst)


	print("sum: " + str(sm))
	print("prod: " + str(pd))
	print(rv)







