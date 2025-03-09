def maker(n):
  def action(x):
    return x*n
  def reaction(x):
    return x**n
  if n > 3:
    return action
  else:
    return reaction
f1 = maker(2)
print (f1)
print (f1(3))
f2 = maker(4)
print (f2(6))
