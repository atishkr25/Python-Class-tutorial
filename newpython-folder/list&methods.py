l1  = [110,251,25,230,45,1.02]
print(l1)
print(type(l1))
# l1.remove("Atish")
print(l1)

print("the count of 11 is: ",l1.count(25))

l1.sort()
print(l1)

l1.pop()
print(l1)

l1.append(100)
print(l1)

# l1.clear()
print(l1)
l1.extend([88,11,22,33])
print(l1)

print(l1.index(100))
print(l1.index(1.02))
print(l1.index(88))
print(l1[1:])
l1[0]=555
print(l1)