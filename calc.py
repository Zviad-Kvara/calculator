# Decorations added by front-end developers
print("I am sexiest function ever\n")

#_______ original code ____________
x = int(input("X: "))
y = int(input("Y: "))

print(f"Sum: {x + y}")
print(f"Sub: {x - y}")

#______  original code END _________

# added multiplication by back_end developers
print(f"Mult: {x * y}")

# added devision by check
if y == 0:
	print("Can't devide")
else:
	print(f"Div: {x / y}")
