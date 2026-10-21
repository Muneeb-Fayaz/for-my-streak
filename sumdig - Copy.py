x=123
s=0

while x>0:
    y=x%10
    x=x//10
    s=y+s
print(s)