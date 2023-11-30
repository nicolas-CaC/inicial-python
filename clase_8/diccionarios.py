dic = {
    'nombre': 'abc',
    'apellido':'def'
}

dic['apellido'] = 'Gomez'
dic['edad'] = 12

print(dic.get('apellido')) 
print(dic)

dic.update({'nombre': 'Hernan', 'edad': 30})
print(dic)

dic.pop('nombre')
print(dic)

print('Gomez' in dic.values())

# for key in dic.keys():
#     print(key)
    
# for key in dic.values():
#     print(key)  

# for key, value in dic.items():
#     print(key, value)
    
    