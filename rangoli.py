size = 5
for i in range(1, size+1):
  print("-"*(2*(size-i)), end="")
  s = chr(96+size)
  for j in range(1,i):
    s= s + ("-"+chr(96+size-j))
  s2 = s[::-1]
  print(s+s2[1::],end="")
  print("-"*(2*(size-i)))
for i in range(size-1, 0, -1):
  print("-"*(2*(size-i)), end="")
  s = chr(96+size)
  for j in range(1,i):
    s= s + ("-"+chr(96+size-j))
  s2 = s[::-1]
  print(s+s2[1::],end="")
  print("-"*(2*(size-i)))