H_weight = 1.00794
C_weight = 12.0107
O_weight = 15.9994

num_H = float(input("Enter number of hydrogen atoms "))
num_C = float(input("Enter number of carbon atoms "))
num_O = float(input("Enter number of oxygen atoms "))
         
weight = (num_H*H_weight) + (num_C*C_weight) + (num_O*O_weight)

print("The molecular weight of the compound is", weight)

