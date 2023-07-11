# list in python are abjects
name = ["m",'bail','kami','bob','salman']
print(name)
print(name[0])
print(name[-1])  # result will be kami
print(name[-2])  # result will be bail

name[1] = 'shan' # replace index 1 string
print(name)
# 0 is the index from where we want to start print and 3 is the index of 
# last item of last uptil there it will print but last one will not print
print(name[0:3]) # it not modify original list it , result=>['m', 'shan', 'kami']
print(name[1:3]) # result=>['shan', 'kami']