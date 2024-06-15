n=int(input())
p=int(input())
time=240
time=time-p
x=1
res=0
while time>0:
      if x*5<time:
         time-=x*5
         x+=1
         res+=1
      else:
         break
print(res)
