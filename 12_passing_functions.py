def sqr(n):
    return n**2
sqr2 = sqr  #making a copy of the function
print(sqr2(5))  #using the copy
del(sqr)  #deleting the original function
print(sqr2(5))
