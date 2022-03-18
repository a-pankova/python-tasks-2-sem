def eat(*x):
  for i in x:
    if i % 2 == 0:
      return "ok"
  return "I like evens"

print(eat(11, 33, 55, 10, 77, 99))
print(eat(1, 33, 555, 7777))
