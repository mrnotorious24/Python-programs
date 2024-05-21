s1 = {10, 20, 30, 40, 60}
s2 = list(s1)
s3 = {40, 50, 30, 40, 60}
s4 = list(s3)
s5 = []  

def intersection(s2, s4):
    for i in s2:
        if i in s4:
            s5.append(i)
    return s5

s5 = intersection(s2, s4)
print("s2:", s2)
print("s4:", s4)
print("Intersection:", s5)
