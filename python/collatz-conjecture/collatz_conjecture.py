def steps(number):
    
    if number<1 or type(number)!=int:raise ValueError("Only positive integers are allowed")
    
    
    count =0
    while number!=1:
        count+=1
        if number&1:#Odd
            number=3*number+1
        else:
            number//=2
        
    return count     

print(steps(16))       
