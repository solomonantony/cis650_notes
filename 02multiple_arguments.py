def minimum(value1, value2, value3, value4):
  """Returns the lowest of four values """
  min_value = value1
  if value2 < min_value: min_value = value2
  if value3 < min_value: min_value = value3
  if value4 < min_value: min_value = value4
  return min_value

coldest_temperature = minimum(-100, 20, 450, -290)
print(coldest_temperature)
minimum(-100, 20, 450, 'abc') # why does this line cause an error? Write your answer below as a comment

