import random

def trunct(num):
    return int(num*1000)/1000

arr = [random.uniform(0.01,0.05) for _ in range(1000000)]

sumnum = 0
sumtrun = 0
for i in arr:
    sumnum = sumnum+i
    sumtrun = trunct(sumtrun+i)

print('Truncat Loss  = ', sumnum-sumtrun)

sumnum1 = 0
sumtrun1 = 0

for i in arr:
    sumnum1 = sumnum1+i
    sumtrun1 = round(sumtrun1+i,2)

print('Round Loss: ',sumnum1-sumtrun1)
