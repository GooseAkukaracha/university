import random

vin1 = 0
vin2 = 0

for i in range(0, 10000):   # Цикл на 10000 значений
    door = [0, 1, 0]    # Вспомогательный список
    doors = random.choice(door)    # Рандомный выбор в списке
    door.remove(doors)
    door.remove(0)
    if doors == 1:  # Блок условия
        vin1 += 1
    elif door[0] == 1:
        vin2 += 1

print(f'Процент выигрыша при своем изначальном выборе: {vin1 // 100}%')
print(f'Процент выигрыша при своем измененном выборе: {vin2 // 100}%')
print('Вывод: Меняйте свой выбор и не ведитесь на ведущего!')






