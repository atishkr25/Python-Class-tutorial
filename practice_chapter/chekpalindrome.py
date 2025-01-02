def chek_palindrome(num):
  original_num = num
  rem=0
  sum=0
  while num>0:
    rem=num%10;
    sum=sum*10+rem;
    num=num//10;
  
  return original_num == sum

num = int(input("Enter a number: "))

if chek_palindrome(num):
  print('palindrome number')

else: 
  print('not a plaindrome number')
