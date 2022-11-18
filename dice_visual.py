import os
import time
import pygal

from dice import Dice

def input_data(checker, message):
    # Ввод информации и количестве кубов, количестве граней куба, 
    # количестве бросков
    while True:
        clear = lambda: os.system('cls')
        clear()

        try:
            data = int(input(message))
        except:
            print('Введите число.')
            time.sleep(3)
        else:
            if checker == True:
                if data > 0:
                    break
                else:
                    print('Введенное значение должно быть больше нуля')
                    time.sleep(3)
            else:
                if data > 0 and data % 2 == 0:
                    break
                else:
                    print('Введенное значение должно быть четным и больше нуля')
                    time.sleep(3)
    return data

dice = []
results = []
dice_sides = []
frequencies = []

dice_numbers = input_data(True, 'Количество кубиков: ')

if dice_numbers > 1:
    approval = input('Количество граней кубика разные? (y/n)')
    if approval == 'y':
        for count in range(dice_numbers):
            dice_sides += [input_data(False, 'Количество граней: ')]
    else:
        dice_sides += [input_data(False, 'Количество граней: ')]
        for count in range(dice_numbers):
            dice_sides += [dice_sides]
else:
    dice_sides += [input_data(False, 'Количество граней: ')]

r_n = input_data(True, 'Количество бросков: ')

print('Количестов кубиков: {}'.format(dice_numbers))
print('Количестов граней: {}'.format(dice_sides))
print('Количестов бросков: {}'.format(r_n))

for d_c in range(1, dice_numbers+1):
    dice += [Dice(dice_sides[d_c - 1])]

if len(dice) > 1:
    for index in range(1, len(dice)):    
        for roll_num in range(r_n):
            result = dice[index-1].roll() + dice[index].roll()
            results += [result]
    print(results)

    for index in range(1, len(dice)):
        max_result = dice[index-1].num_sides + dice[index].num_sides

    for index in range(1, len(dice)):
        for value in range(dice_numbers, max_result + 1):
            frequency = results.count(value)
            frequencies += [frequency]
    print(frequencies)
else:   
    for roll_num in range(r_n):
        result = dice[0].roll()
        results += [result]
    print(results)

    for value in range(1, dice_sides[0] + 1):
        frequency = results.count(value)
        frequencies += [frequency]
    print(frequencies)

hist = pygal.Bar()
hist.title = "Резульаты n бросков m куба/ов d{}".format(dice_sides)
hist.title += "\n n = {}; m = {}".format(r_n, dice_numbers)
if dice_numbers > 1:
   for count in range(dice_numbers):
        max_result = dice_numbers*dice_sides[count] + 1
        hist.x_labels = list(range(dice_numbers, max_result))
else:
    hist.x_labels = list(range(dice_numbers, (dice_numbers*dice_sides[0]) + 1))
hist.x_title = 'Результы'
hist.y_title = 'Частота результатов'

hist.add('d{}'.format(dice_sides), frequencies)
hist.render_to_file('dice_visual.svg')