# a=65
# # ans=float(a**0.5)
# print(a**0.5)

a=int(input("enter a: "))
b=int(input("enter b: "))
c=int(input("enter c: "))

d=b*b-4*a*c
root1= (-b+(d**0.5))/2*a
root2= (-b-(d**0.5))/2*a

# if(d < 0){ print('') }
print('root1: ',root1,'root2: ',root2)
