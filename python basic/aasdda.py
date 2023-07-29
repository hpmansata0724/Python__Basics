l2 = (1, 2, 3, 4)  # tuple
l3 = {1, 2, 3, 4, 5, 5, 5}  # set
l4 = {"name": "dhruv"}  # dict


# print(l1, l2, l3, l4)

#
def fun(i):
    if i <= 5:
        return True
    else:
        return False


a = []
l1 = [1, 12, 3, 4]  # list
a = list(filter(fun, l1))
print(a)

# a = {}
# l1 = {1, 12, 3, 4}  # list
# fun = lambda i: i + 1
# a = set(map(fun, l1))
# print(a)
