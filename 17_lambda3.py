#This is a shorthand for def, in place of three defs, we use an array of lambdas

lambdas = [lambda x: x ** 2,
         lambda x: x ** 3,
         lambda x: x ** 4]
print(lambdas[0](2))
print(lambdas[1](2))

#does it make sense?
