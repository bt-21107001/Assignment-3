#User gets instructions
print("Welcome to python calculator program.")
print("Type a mathematical expression.")
print("Instructions:")
print("+ and - have their usual meaning.")
print("Use * for multiplication, / for divsion.")        
print("Use ** for exponent.")
print("Input only numbers and signs stated above.")

#User enters an input as a math expression
output = input()

#Use eval function to evaluate the expression, it gives value of the math expression
result = eval(output)

print("Value of the expression is",result)
