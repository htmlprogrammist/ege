start, end = 3144472, 3144600

def isPrime( x ):
  if x <= 1: return False
  d = 2
  while d*d <= x:
    if x % d == 0:
      return False
    d += 1
  return True

count = 0
for x in range( start, end+1 ):
  if isPrime( x ):
    count += 1
    print( count, x )

