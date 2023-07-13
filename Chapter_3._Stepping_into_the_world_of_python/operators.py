a = 12
b = 3

# arithmatic operator
print(a + b)
print(a - b)
print(a * b)
print(a/b)      # output --> float
print(a//b)     # output --> int (integer division, rounded down towards minus infinity)
print(a%b)      # modulo: output --> remainder

#operator precidance/ default execution sequence = division(/) OR multiplication(*) --> addition(+) OR substraction(-)
# BODMAS = Brackets, Order(Exponents), Division/Multiplication, Addition/substraction 
print(a+b / 3-4 * 12) # -35.0