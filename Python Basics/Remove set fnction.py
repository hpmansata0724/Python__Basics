s1={'Physics','Chemistry','Maths','Biology'}
print(s1)
s1.remove("Maths")
print("After removing:",s1)
s2={'Physics','Chemistry','Maths','Biology'}
print(s2)
s2.discard("Sci")
print("After discarding:",s2)
s3={'Physics','Chemistry','Maths','Biology'}
print(s3)
s3.pop()
print("After pop method:",s3)
s3.clear()
print("After clearing:",s3)
del s2
print("After del keyword:",s3)

