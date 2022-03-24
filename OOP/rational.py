from math import gcd

class Rational:

  def __init__(self, __n, __d=1):
    _gcd = gcd(__n, __d)
    self.__n = int(__n / _gcd)
    self.__d = int(__d / _gcd)
    if self.__n < 0 and self.__d < 0:
      self.__n = abs(self.__n)
      self.__d = abs(self.__d)

  def get_n(self):
    return self.__n

  def get_d(self):
    return self.__d

  def __str__(self):
    if self.__d == 1:
      return str(self.__n)
    elif self.__n == 0:
      return '0'
    elif self.__n == self.__d:
      return '1'
    else:
      return f"{self.__n}/{self.__d}"

  def as__number(self):
    return round(self.__n/self.__d, 5)

  def __add__(self, other):
    return Rational(self.__n * other.__d + self.__d * other.__n, self.__d * other.__d)

  def __sub__(self, other):
    return Rational(self.__n * other.__d - self.__d * other.__n, self.__d * other.__d)

  def __mul__(self, other):
    return Rational(self.__n * other.__n, self.__d * other.__d)

  def __truediv__(self, other):
    return Rational(self.__n * other.__d, self.__d * other.__n)

  def __iadd__(self, other):
    self.__n = self.__n * other.__d + self.__d * other.__n
    self.__d = self.__d * other.__d
    _gcd = gcd(self.__n, self.__d)
    self.__n = int(self.__n / _gcd)
    self.__d = int(self.__d / _gcd)
    return self

  def __isub__(self, other):
    self.__n = self.__n * other.__d - self.__d * other.__n
    self.__d = self.__d * other.__d
    _gcd = gcd(self.__n, self.__d)
    self.__n = int(self.__n / _gcd)
    self.__d = int(self.__d / _gcd)
    return self

  def __imul__(self, other):
    self.__n = self.__n * other.__n
    self.__d = self.__d * other.__d
    _gcd = gcd(self.__n, self.__d)
    self.__n = int(self.__n / _gcd)
    self.__d = int(self.__d / _gcd)
    return self

  def __itruediv__(self, other):
    self.__n = self.__n * other.__d
    self.__d = self.__d * other.__n
    _gcd = gcd(self.__n, self.__d)
    self.__n = int(self.__n / _gcd)
    self.__d = int(self.__d / _gcd)
    return self

  def __eq__(self, other):
    return self.__n == other.__n and self.__d == other.__d

  def ___nq__(self, other):
    return self.__n != other.__n or self.__d != other.__d

  def __lt__(self, other):
    return self.__n * other.__d < other.__n * self.__d

  def __le__(self, other):
    return self.__n * other.__d <= other.__n * self.__d

  def __gt__(self, other):
    return self.__n * other.__d > other.__n * self.__d

  def __ge__(self, other):
    return self.__n * other.__d >= other.__n * self.__d

num1 = Rational(-1, 4)
num2 = Rational(10, 5)
print(f"num1.__str__() = {num1.__str__()}")
print(f"num1.as__number() = {num1.as__number()}")

num3 = num1.__add__(num2);
print(f"\n{num1} + {num2} = {num3}")
print(f"{num1} - {num3} = {num1 - num3}")
print(f"{num2} += {num3} = ", end='')
num2 += num3
print(num2)
print(f"{num2} -= {num3} = ", end='')
num2 -= num3
print(num2)
print(f"{num2} *= {num3} = ", end='')
num2 *= num3
print(num2)
print(f"{num2} /= {num3} = ", end='')
num2 /= num3
print(num2)
num3 -= num1
print(f"{num3+num1} - {num1} = {num3}")
num4 = num1 * num2
print(f"{num1} * {num2} = {num4}")
print(f"{num4} / {num3} = {num4/num3}")
num5 = Rational(-4, 8)
print(f"{num4} == {num5} {num4==num5}")
print(f"{num4} == {num3} {num4==num3}")
print(f"{num2} < {num3} {num2<num3}")
print(f"{num2} <= {num3} {num2<=num3}")
print(f"{num1} > {num5} {num1>num5}")
print(f"{num4} >= {num4} {num4>=num4}\n")

print(num4.get_n())
print(num4.get_d(), '\n')

def countOrder(n: int):
  if n == 0:
    return "invalid value"
  sign = 1
  out = 0
  if n < 0:
    sign = -1
    n = -n
  for i in range(1, n+1):
    out += 1/i
  return out*sign

print(countOrder(1))
print(countOrder(2))
print(countOrder(3))
print(countOrder(-3))

