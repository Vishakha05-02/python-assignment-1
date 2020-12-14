# Question1
lst = []
for i in range(2000, 3200):
    if (i % 7 == 0) and (i % 5 != 0):
        lst.append(i)
print(lst, end='')

# Question2
f_name = input("Enter first name: ")
l_name = input("Enter last name: ")
print(l_name + ' ' + f_name)

# Question3
pi = 3.1415926535897931
d = 12
r = float(d/2)
v = float((4.0/3.0)*pi*(r**3))
print('volume of sphere is', v)

