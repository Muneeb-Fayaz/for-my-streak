x=123
s=0
while x>0:
    y=x%10
    s=s*10+y
    x=x//10
print(s)