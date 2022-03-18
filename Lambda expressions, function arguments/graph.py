def func_task1(x):
  return x * x

def graph(f):
  for i in range(11):
    print(f"f({i}) = {(f(i))}")

graph(func_task1)

func_task2 = lambda x: x * x

graph(func_task2)

def graph_n(f, n=10):
  for i in range(n+1):
    print(f"f({i}) = {(f(i))}")

graph_n(func_task2, 15)
graph_n(func_task2)

def graph_nm(f, n=10, m=20):
  for i in range(n, m+1):
    print(f"f({i}) = {(f(i))}")

graph_nm(func_task2, m=15)
