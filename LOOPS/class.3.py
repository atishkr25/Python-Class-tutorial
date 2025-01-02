# age=int(input("input a number  "))
# if(a%2==0):
#   print(a+1)
# else:
#  print(a+2)

# age = int(input('enter Age: '))
# if age>0:
#   if age >18 :
#     print('You are above 18')
#   else :
#     print('You are below 18')  

# else:
#   print('Cant be less than 0 ')

# if age <= 0:
#   print('Cant be less than 0')
# elif 0<age<18:
#   print('Age is less than 18')
# else :
#   print('Age is above 18')

# x=3
# if x>2 or x<5 and x==6:
#  print("ok")
# else :
#  print("no")

# y=0.1*3
# if y!=0.3:
#  print("launch a missile")
# else :
#  print("NO")

# print(y)

# x=10
# if(x>2):
#   x=x*2;
# if(x>4):
#   x=0;
# print(x)

a = int(input("enter num"))
sum=0;

for i in range(1,a+1,2):
  sum+=i;
print(sum)