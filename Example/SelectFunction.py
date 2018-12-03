def add(a,b):
	return a+b

def sub(a,b):
	return a-b

select = 0
result = (add,sub)[select](2,3)
print(result)
