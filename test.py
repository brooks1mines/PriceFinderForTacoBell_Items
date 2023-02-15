import decimal
import time

def prange(x, y, jump):
  while x < y:
    yield float(x)
    x += decimal.Decimal(jump)

def nrange(x, y, jump):
  while x > y:
    yield float(x)
    x += decimal.Decimal(jump)

lats = list(prange(25,49,'0.142857'))
longs = list(nrange(-66,-125,'-0.1667'))
for i in lats:
  for j in longs:
    print(i,j)

# how to determine time during a program

#t = time.localtime(time.time())
#while True:
  #t = time.localtime(time.time())
  #print(t.tm_hour, t.tm_min, t.tm_sec)

new_lats = myRange(25,50,0.142857)
new_longs = myRange(-66,-125,-0.1667)

#for i in lats:
  #for j in new_longs:
   # print(i,j)