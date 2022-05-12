#User enters number
inp_number = int(input("Enter number to convert into binary. "))

#bin function coverts integer value into binary

bin_number = bin(inp_number)
bin_displayed = bin_number[2:]

print("Binary equivalent of entered number is:",bin_displayed)
