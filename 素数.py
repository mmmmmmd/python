N=100
result = []
for num in range(2,N):
  f=True
  for snu in range(2,num-1):
    if num % snu == 0:
      f=False
      break
  if f:
    result.append(num)
print result
