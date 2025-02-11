from math import sqrt

start, end = 173225, 217437

def isPrime( x ):
  if x <= 1: return False
  d = 2
  while d*d <= x:
    if x % d == 0:
      return False
    d += 1
  return True

minOK = 0
count = 0
for i in range(start, end+1):
  q = round(sqrt(i))
  D = [2] + list( range(3, q+1, 2) )
  for x in D:
    if i % x == 0 and isPrime(x):
      y = i // x
      if x != y and isPrime(y) and (x % 10 == y % 10):
        count += 1
        if minOK == 0:
          minOK = i
        break

print( count, minOK )

