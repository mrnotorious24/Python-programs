s1 = {10, 20, 30}
s2 = list(s1)
s3 = {40, 50, 30}
s4 = list(s3)
s5 = []  # Initialize s5 as an empty list

def ope(s2, s4):
    for i in s2:
        s5.append(i)  # Append elements of s2 to s5
    for j in s4:
        if j not in s5:
            s5.append(j)  # Append elements of s4 not in s5

ope(s2, s4)  # Call the function passing s2 and s4
print("s2:", s2)
print("s4:", s4)
print("s5:", s5)
