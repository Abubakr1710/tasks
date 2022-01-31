length=int(input("Length of list:"))  #gets length of list from user 
list=[]
for i in range(length):
    a=int(input()) #gets index of list
    list.append(a) #add index to the list

for i in set(list): #set collection
    if list.count(i)==1: #count returns the number of elements with the specified value. if list.count(i)==1: checks for non duplicate 
        print("This one is non duplicate: ",i)