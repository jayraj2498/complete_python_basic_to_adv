def check_temp(temp,unit) : 
    if unit =='C' :
        return  temp * 9/5 + 32  # c to F
    
    if unit =='F' :
        return (temp-32)*5/9  # f to C  
    
    else : 
        return False 
    
    
    
    
def is_str_pass(password) : 
    "this is func to check pass is storng  or not" 
    
    if len(password) < 8 :
        return False 
    
    if not any(char.isdigit()  for char in password) :
        return False 
    
    if not any(char.islower() for char in password) :
        return False 
    
    if not any(char.isupper() for char in password) : 
        return False  
    
    if not any(char in "@#%$&*()_+!" for char in password) : 
        return False    
    
    
    return True 




def simple_intrest(pa:int,ri:int,tp:int):
    print(" your are in simple intrest function ") 
    
    result= pa*ri*tp/100
    return result
    
    
    
    
def my_fun(word1,word2):
    result= word1 +" "+ word2
    # print(f"{result}")
    return result 




def even_odd(ip):
    if ip%2==0:
        print(f"even :{ip}")
    else:
        print(f"odd:{ip}")