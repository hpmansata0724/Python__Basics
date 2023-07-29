s=("Heyram said:Quality is show our Silent Personality")
print("Is this string start with 'hey':",end="")
if(s.startswith("Hey")):
    print("Yes")
else:
    print("No")
print("Is this string end with 'be':",end="")
if(s.endswith("Silent")):
    print("Yes")
else:
    print("No")
print("Split string is:",s.split())
print("Replace 'm' instead of 't' in string:",s.replace('t','m'))
print("Delete string is:")
del s
s1="Hey"
s2="Ram!"
print("s1+s2=",(s1+s2))
print("s1*3=",(s1*3))