#SAI VARDHAN 'S SOLUTION - PASSED ALL TEST CASES

n=input().split()
try:
  for i in range(len(n)):
    n[i]=int(n[i])
    if n[i]<0:
      raise Exception
  o=[]
  for i in n:
    if i%2==0:
      if i>3 and i<5:
        o.append('Not Weird')
      elif i>7 and i<21:
        o.append('Weird')
      else:
        o.append(-1)
    elif i%2!=0:
      if i>33:
        o.append('Not Weird')
      elif i==5:
        o.append(-2)
      else:
        o.append('Weird')
  print(o)
except:
  print("Error!")
