print("елка")#команда

a = 10                  #коробка с числом 
a = 'елка'              #коробка со строкой
a = [1, 2, 'g', 3, 'r']   #коробка с списком
print(a)

import random           #подключаем библиотеку
r = random.randint(1,5) #используем библиотеку

if r == 1:              #если 
	print('OK')
elif r == 2:            #тоже если
	print('ne OK') 
else:                   #иначе(если if не работает) 
	print('...')
