# ask user for name 
# example - "Vanshika"
#print count of each words
# output:
        #   V : 1
        #   a : 2
        #   n : 1
        #   s : 1
        #   h : 1
        #   i : 1
        #   k : 1
        #   a : 2


#ans:
name = input("enter a name : ")
temp = "" 
for i in range (0,len(name)):
    if name[i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")
        temp += name[i]

