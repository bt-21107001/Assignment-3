import math

#a
answer_1 = (3+4)*5
print("Answer (a):", answer_1)


#b
n = float(input("Enter Number"))
answer_2 = (n*(n-1))/2
print("Answer (b):", answer_2)


#c
radius = float(input("Enter Number"))
answer_3 = 4*math.pi*(radius**2)        
print("Answer (c):", answer_3)


#d
r = float(input("Enter Number"))
angle = float(input("Enter Angle in Radians"))
b = math.cos(angle)
c = math.sin(angle)
answer_4 = (r*(b)**2 + r*(c)**2)**(1/2)
print("Answer (d):", answer_4)


#e
y1 = float(input("Enter Number y1"))
y2 = float(input("Enter Number y2"))
x1 = float(input("Enter Number x1"))
x2 = float(input("Enter Number x2"))
answer_5 = ((y1 - y2)/(x1 - x2))
print("Answer (e):", answer_5)
