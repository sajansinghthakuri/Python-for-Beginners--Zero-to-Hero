#Arithmetic Operators

#  Add, Subtract, Multiply, Divide, Modulus, Exponent, Floor Division
# +, -, *, /, %, **, //

x= 10
y=3

print(x+y)  #10+3=13
print(x-y)  #10-3=7
print(x*y)  #10*3=30
print(x/y)  #10/3=3.33
print(x%y)  #10%3=1
print(x**y) #10*10*10=1000
print(x//y) #10//3=3






#Comparison Operators
# >, <, ==, !=, >=, <=

print(x>y)  #True
print(x<y)  #False
print(x==y) #False
print(x!=y) #True
print(x>=y) #True
print(x<=y) #False




#Logical Operator
# And, Or, Not

a,b= True, False
print(a and b)  # False (Both a and b must be true)
print(a or b)   # True (either a or b should be true)
print(not a)    #False


#Assignment Operator
# +=, -=, *=, /=

x=5
x+=2    #x=x+2
x-=3    #x=x-3
x*=5    #x=x*5
x/=2    #x=x/2



#Membership Operator
# in, not in

nums =[1,2,3]
print(2 in nums )   #True
print(8 not in nums)    #True



#Identity Operators
#is, not is

x=[1,2,3]
y=x
print(x is y)   #True
print(x is not y)   #False

