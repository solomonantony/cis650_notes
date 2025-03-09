def f(a,b,c):
    print (a,b,c)

f(1,2,3) # 1 Any keyword argument?
f(c=3, b=2, a= 1) #2   Any positional arguments?
f(1, c=3, b=2)  #3 Which are positional arguments?
f(a='Bob', b=40, c='dev') #4
f(12, a='1', 2) #5 Why can't we have a positional argument following a keyword argument?
