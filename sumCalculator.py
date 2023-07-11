# input will always return string so we are converting to to float so we can add to numbers
# if we add without convertion. the result will not be sum instead it will concat to strings

first = float(input('first: ')) 
second = float(input('second: '))

sum = first + second
# we are converting sum because we can not concat string with int,float and bool
print('Sum : '+ str(sum))
