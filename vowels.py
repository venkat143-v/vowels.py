def test(x): 
 vowels="AEIOUaeiou" 
 for ch in x: 
 if ch in vowels: 
 return x,"contains vowels" 
 break 
 else: 
 return(x,'no vowels') 
x=input() 
k=test(x) 
print(k)
