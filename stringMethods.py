# upper and lower function will not convert the original value it will give us a new value
# find will start from 0 index 
course = "Python for beginners"

print(course.upper())
print(course.lower())
print(course.find('y')) # result =>1 
print(course.find('Y')) # result =>-1 because Y is not present 
print(course.find('for')) # result=> 7 count white spaces as well 
print(course.replace('for', '4')) 
print(course.replace('x', '4')) # x not present so nothing happens
print('Python' in course) # will return True
