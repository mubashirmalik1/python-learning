# range will give number up to the number we provide like in below example 5 so it will give 0,1,2,3,4
numbers = range(5)  
print(numbers) #it will show the range not the value to print values we can use for loop
for number in numbers:
    print(number)

# we can also provide start and end range as well
numbers = range(5 ,10)  
print(numbers) 
for number in numbers:
    print(number)


# we can also provide start and end range and jump point as well
numbers = range(5 ,10, 2)  
print(numbers) 
for number in numbers:
    print(number) # result 5,7,9 