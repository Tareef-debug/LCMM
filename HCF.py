#Pogram to HCF/Gcd(Greatest Common Divisor)
n1=int(input("Enter the larger number"))
n2=int(input("Enter the smaller number"))
while(n2):
    x = n2 
    n2 =n1 % n2
    n1 = x
print("Hcf Is", n1)