items = [5, 7, 10, 12, 15]
print("List of items is", items)
x = int(input("Enter item to search: ")) 
i = flag = 0
while i < len(items):
    if items[i] == x:  
        flag = 1
        print("Item found at position:", i + 1)
        break  
    i += 1  
if flag == 0: 
    print("Item not found")
