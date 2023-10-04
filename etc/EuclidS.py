def gcd(a , b):
    c = a % b
    if c == 0:
        return b

    return gcd(b,c)

a = 10 
b = 15
print("g(",a,",",b,") = ",gcd(a,b))
a = 35 
b = 10
print("g(",a,",",b,") = ",gcd(a,b))
a = 31 
b = 2
print("g(",a,",",b,") = ",gcd(a,b))
a = 2877
b = 7398
print("g(",a,",",b,") = ",gcd(a,b))
a = 0
b = 102
print("g(",a,",",b,") = ",gcd(a,b))
