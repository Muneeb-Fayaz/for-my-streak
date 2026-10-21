x = 153

t = x

s = 0

while x > 0:
 
    ld = x % 10
    
    cube = ld * ld * ld
    
    s = s + cube
    
    x = x // 10

if t == s:
    print("Yes, 153 is an Armstrong number.")
else:
    print("No, 153 is not an Armstrong number.")
