import numpy as np
x = np.array([2,-1,0,1,2])
np.absolute(x)
print(x)


x = [1,2,3]
print(np.exp(x))

print("__"*22)
#creating an array using arange functin
x = np.arange(5)
print(x)

print("____"*20)
x=np.arange(1,11)
np.add.reduce(x)
print(x)

print("__"*20)

ans = np.add.accumulate(x) #method for finding prefix sum 
print(ans)
print("__"*20)

sum_val = np.sum(x) #method for finding the sum of the array
print(sum_val)
print("__"*20)

x= np.arange(1,6)
product_value = np.prod(x) #methods to finding the product of the given element , 
print(product_value)
print("__"*20)

mean = np.mean(x)
print(mean)
print("__"*20)

maxi = np.max(x)
print(maxi)
print("__"*20)

mini = np.min(x)
print(mini)
print("__"*20)

#rearanging array 
a = np.arange(2,11)
print(a)
a = np.arange(1,101).reshape(10,10)
print(a)
first_column = a[:, 0]  # Slice all rows and only the 1st column
print("\nAll rows, 1st column:")
print(first_column)

