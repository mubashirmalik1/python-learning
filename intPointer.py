# if variable num1 and num2 have same value then it value will have one address
# e.g num1 =11 , num2 = num1 => it will have same address 
#num1 =11 , num2 = 11 => it will have same address as well

num1 = 11

num2 = num1

print('Print before num2 value update')
print('numb1:',str(num1))
print('numb2:',str(num2))

print('get the address of num1 and num2')
print('numb1:',id(num1))
print('numb2:',id(num2))

num2 =22

print('Print after num2 value update')
print('numb1:',str(num1))
print('numb2:',str(num2))

print('get the address of num1 and num2')
print('numb1:',id(num1))
print('numb2:',id(num2))