from functools import reduce
'''The reduce(fun,seq) function is used to apply a particular function
passed in its arguement to all the list elements mentioned i the sequence
passed along.The Function is defined in "functools"module.
'''
l1=[1,2,3,4,5]
s=reduce(lambda a,b:a+b,l1)
m=reduce(lambda a,b:a9ol if a>b else b,l1)
print("l1",l1)
print("Sum of all elements using reduce functions:",s)
print("Max from all elements using reduce function :",m)