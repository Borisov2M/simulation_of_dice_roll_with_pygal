import os
import time
import pygal

from dice import Dice

dice = []
results = []
dice_sides = []
frequencies = []
approval_input = False

dice_numbers = Dice.input_data(True, 'Количество кубиков: ') # Ввод количества 
                                                             #кубиков

#*************** Ввод граней в зависимости от количества кубиков ***************
if dice_numbers > 1:  
    #------------------- Проверка правильности ввода ответа --------------------
    while approval_input == False:
        approval = input('Количество граней кубика разные? (y/n)\n')
        if approval == 'y' or approval == 'n':
            approval_input = True
        else:
            print('Вы дали неверный ответ.')
            time.sleep(1)
            clear = lambda: os.system('cls')
            clear()
    #---------------------------------------------------------------------------
    #----- Ввод количества граней в зависимости от различия граней кубиков -----
    if approval == 'y':
        for count in range(dice_numbers):
            dice_sides += [Dice.input_data(False, 'Количество граней: ')]
    else:
        side = Dice.input_data(False, 'Количество граней: ')
        for count in range(dice_numbers):
            dice_sides += [side]
    #---------------------------------------------------------------------------
else:
    dice_sides += [Dice.input_data(False, 'Количество граней: ')]
#*******************************************************************************

r_n = Dice.input_data(True, 'Количество бросков: ') # Количество бросков каждого
                                                    # кубика

#************************* Вывод информации о кубиках **************************
print('Количестов кубиков: {}'.format(dice_numbers))
print('Количестов граней: {}'.format(dice_sides))
#*******************************************************************************

#******* Создание списка объектов класса по количеству брощенных кубиков *******
for d_c in range(dice_numbers):
    dice += [Dice(dice_sides[d_c])]
#*******************************************************************************


#********* Рассчет результатов бросков и частоты выпадения результатов *********
if len(dice) > 1:      
    for roll_num in range(r_n):
        for index in range(dice_numbers):
            result = dice[index-1].roll() + dice[index].roll()
        results += [result]
    print(f'Список результатов бросков: {results}')

    max_result = dice[0].num_sides
    for index in range(1, dice_numbers):
        max_result += dice[index].num_sides
    print(f'Максимальный результат броска: {max_result}')

    for value in range(dice_numbers, max_result + 1):
        frequency = results.count(value)
        frequencies += [frequency]
    print(f'Частота выпадения значения на кубиках: {frequencies}')
else:   
    for roll_num in range(r_n):
        result = dice[0].roll()
        results += [result]
    print(f'Список результатов бросков: {results}')

    for value in range(1, dice_sides[0] + 1):
        frequency = results.count(value)
        frequencies += [frequency]
    print(f'Частота выпадения значения на кубике: {frequencies}')
#*******************************************************************************

#***************************** Создание svg файла ******************************
hist = pygal.Bar()
hist.title = "Резульаты n бросков m куба/ов d{}".format(dice_sides)
hist.title += "\n n = {}; m = {}".format(r_n, dice_numbers)

#----------------- Отрисовка гистограммы результатов бросков -------------------
if dice_numbers > 1:
    if approval == 'y':
        for count in range(1, dice_numbers):
            maxresult = dice_numbers*dice_sides[count] - 1
        hist.x_labels = list(range(dice_numbers, maxresult))
    else:
        maxresult = dice_numbers*dice_sides[0] + 1
        hist.x_labels = list(range(dice_numbers, maxresult))
else:
    maxresult = dice_numbers*dice_sides[0] + 1
    hist.x_labels = list(range(1, dice_sides[0] + 1))
#-------------------------------------------------------------------------------

hist.x_title = 'Результы'
hist.y_title = 'Частота результатов'
hist.add('d{}'.format(dice_sides), frequencies)
hist.render_to_file('dice_visual.svg')
#*******************************************************************************