#         0123456789.......
parrot = "Norwegian Blue"

print(parrot)
print(parrot[3]) # w is at index 3 in string parrot

#negative indexing
print(parrot[-1])   # e is the at the -1 index in the string parrot
print(parrot[-14])  # N


#========================

# string slicing

print(parrot[0:9]) # Norweg
print(parrot[0:9:3])

print(parrot[:3])   # Nor
print(parrot[3:])   # wegian Blue

print(parrot[:])    # Norwegian Blue
print(parrot[-4:-2]) # Bl
print(parrot[-4:12]) # Bl