def chek_armstrong(num):
  original_num = num
  digits_len = len(str(num))
  sum=0
  rem =0
  while num>0:
    rem= num%10
    sum = sum+rem**digits_len
    num=num//10

  return original_num==sum

num = int(input("Enter any number: "))

if chek_armstrong(num):
  print(num,'is armstrong')
else:
  print(num,'is not armsrong')  
