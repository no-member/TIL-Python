print('dictionary')
lux = {'health': 800, 'mana': 334, 'melee': 550, 'armor': 18.72}
print(lux)
x = {100: 'hundred', False: 0, 3.5: [3.5, 3.5],
     'hi my friend': {'name': 'shin', 'age': 26}}
print(x)

lux1 = dict(health=490, mana=334, melee=550)
print('lux1', lux1)

lux2 = dict(zip(['health', 'mana', 'melee'], [500, 334, 550]))
print('lux2', lux2)

lux3 = dict([('health', 490), ('mana', 550), ('melee', 334), ('armor', 18)])
print('lux3', lux3)

lux4 = dict({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72})
print('lux4', lux4)
print()

print('딕셔너리 값에 접근하기')
print('lux["health"]', lux['health'])

print()
print('in?')
print('health' in lux4)
print('health' not in lux4)

print()
print('딕셔너리의 길이')
print(len(lux)) 
