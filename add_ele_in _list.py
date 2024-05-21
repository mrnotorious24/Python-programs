#creating an empty list
list1 = []

#no of elements as input
n = int(input("enter the number of elements:"))

#iterating till the range
for i in range(0,n):
    ele = int(input())
    list1.append(ele) #adding the element
    
    print("list after initial elements:",list1)
    
    #promt for additional elelments
    n = int(input("enter number additional elements: "))
    
    #adding additional elements to the list
    for i in range(0,n):
        ele1 = int(input())
        list1.append(ele1)#adding the element
    
    print("list after adding additional element:",list1)
    
    #prompt for index to be printed
    p=int(input("Enter the index from the list to be printed:"))
    try:
        index = list1.index(p)
        print("the element at index",index,"in the list is:",p)
    except ValueError:
        print("element",p,"not found in the list.")
    
