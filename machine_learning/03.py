import numpy as np
def AND(x1, x2):
  x=np.array([x1, x2])
  w=np.array([0.1, 0.1])
  b=-0.1
  tmp=np.dot(w, x) + b
  if tmp<=0:
    return 0
  else:
    return 1
def OR(x1, x2):
  x=np.array([x1, x2])
  w=np.array([0.5, 0.5])
  b=-0.1
  tmp=np.dot(w, x) + b
  if tmp<=0:
    return 0
  else:
    return 1
def NAND(x1, x2):
  x=np.array([x1, x2])
  w=np.array([-0.5, -0.5])
  b=1
  tmp=np.dot(w, x) + b
  if tmp<=0:
    return 0
  else:
    return 1
def XOR(x1, x2):
    return AND(NAND(x1,x2),OR(x1,x2))


for xs in [(0, 0), (0,1), (1,0), (1,1)]:
  y=AND(xs[0], xs[1])
  print(str(xs) + "=>"+str(y))
print()
for xs in [(0, 0), (0,1), (1,0), (1,1)]:
  y=OR(xs[0], xs[1])
  print(str(xs) + "=>"+str(y))
print()
for xs in [(0, 0), (0,1), (1,0), (1,1)]:
  y=NAND(xs[0], xs[1])
  print(str(xs) + "=>"+str(y))
print()


for xs in [(0, 0), (0,1), (1,0), (1,1)]:
    y = XOR(xs[0], xs[1])
    print(str(xs) + "=>"+str(y))
print()

