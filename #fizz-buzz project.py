#fizz-buzz project
for n in range (1,101):
  if n%3 == 0 and n%5 == 0:
    n='fizz buzz'
  elif n % 3 == 0:
    n='fizz'
  elif n%5 == 0:
    n='buzz'
  
  print (n)