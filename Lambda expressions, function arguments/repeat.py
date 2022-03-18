def repeat(**y):
  lst = []
  for key, val in y.items():
    lst += [key for i in range(val)]
  return lst

print(repeat(hello=2, cat=3))
