dict1 = {
    'value': 11
}

dict2 = dict1

print('Print before dic2 value update')
print('numb1:',str(dict1))
print('numb2:',str(dict2))

print('get the address of num1 and num2')
print('numb1:',id(dict1))
print('numb2:',id(dict2))

dict2['value'] = 22

print('Print after num2 value update')
print('numb1:',str(dict1))
print('numb2:',str(dict2))

print('get the address of num1 and num2')
print('numb1:',id(dict1))
print('numb2:',id(dict2))