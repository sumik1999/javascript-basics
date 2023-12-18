
carry = 0
digits = [1,2,3]  
for i in range(len(digits)-1,0,-1):
    
    curr_digit = digits[i]
    if i==(len(digits)-1):
        digits[i]=(digits[i]+1)%10+carry
    else:
        digits[i]=digits[i]+carry
    
    if curr_digit+1 > 9:
        carry=1
    else:
        carry=0
print(digits)