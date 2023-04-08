import math

print("Please enter the a, b, c and d with this format: a*x^3 + b*x^2 + c*x + d")
a= float(input("Enter a: "))
b= float(input("Enter b: "))
c= float(input("Enter c: "))
d= float(input("Enter d: "))

if a == 0:
    print("Opppps, a cannot be zero, run again")

else:
    print("Your Equation is: " , a , "x^3  +" , b , "x^2  +" , c , "x  +" , d)

delta = (18*a*b*c*d) - (4*(b**3)*d) + ((b**2)*(c**2)) - (4*a*(c**3)) - (27*(a**2)*(d**2))

# p = b - (a**2/3)
# q = (2*a**3/27) - (a*b/3) + c

# delta = (q**2/4) + (p**3/27)
 
if delta > 0:
    print("Δ = " , delta)
    print("The equation has three distinct real roots")
    

if delta == 0:
    print("Δ = " , delta)
    print("The equation has a repeated root and all its roots are real")
    

if delta < 0:
    print("Δ = " , delta)
    print("The equation has one real root and two non-real complex conjugate roots")
    






