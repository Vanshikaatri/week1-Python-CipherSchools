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
        
# ans :
name =input("enter your name : ")
# vanshika
# name.count("v") , name.count(name[0]) = 1
# name.count("a") , name.count(name[1]) = 2
# name.count("n") , name.count(name[2]) = 1
# name.count("s") , name.count(name[3]) = 1
# name.count("h") , name.count(name[4]) = 1
# name.count("i") , name.count(name[5]) = 1
# name.count("k") , name.count(name[6]) = 1
# name.count("a") , name.count(name[7]) = 2

#output
        #   V : 1
        #   a : 2
        #   n : 1
        #   s : 1
        #   h : 1
        #   i : 1
        #   k : 1
        #   a : 2
i = 0
temp_var = ""
while i< len(name):
    if name[i] not in temp_var:
        temp_var +=name[i] 
        print(f"{name[i]} : {name.count(name[i])}")
        i+=1
