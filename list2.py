bike = ['suzuki','harley', 'ducati', 'honda'] 

bike.append('yamaha')
bike.append('kawasaki')

print(bike)

bike.insert(2,'bmw')

print(bike)

del bike[bike.index('yamaha')]

print(bike)

popped_val = bike.pop(4)
bike.append('ducati')

print(bike)
print(popped_val)


bike.remove('ducati')

print(bike)