def multi_add(start, *args):
  result = start
  for x in args:
    result = result + x
  return result

print(multi_add(10, 4, 5, 1, 9, 10))