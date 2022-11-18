import pygal

from dice import Dice

dice = []
results = []
dice_sides = []
frequencies = []

dice_numbers = 5#Dice.input_data(True, 'Количество кубиков: ')
if dice_numbers > 1:
    approval = 'n'#input('Количество граней кубика разные? (y/n)')
    if approval == 'y':
        for count in range(dice_numbers):
            dice_sides += [Dice.input_data(False, 'Количество граней: ')]
    else:
        side = 6 #Dice.input_data(False, 'Количество граней: ')
        for count in range(dice_numbers):
            dice_sides += [side]
else:
    dice_sides += [Dice.input_data(False, 'Количество граней: ')]
r_n = 100 #Dice.input_data(True, 'Количество бросков: ')



print('Количестов кубиков: {}'.format(dice_numbers))
print('Количестов граней: {}'.format(dice_sides))
print('Количестов бросков: {}'.format(r_n))



for d_c in range(dice_numbers):
    dice += [Dice(dice_sides[d_c])]



if len(dice) > 1:
    for index in range(1, len(dice)):    
        for roll_num in range(r_n):
            result = dice[index-1].roll() + dice[index].roll()
            results += [result]
    print(results)

    for index in range(1, len(dice)):
        max_result = dice[index-1].num_sides + dice[index].num_sides
    print(max_result)

    for index in range(1, len(dice)):
        for value in range(dice_numbers, max_result):
            frequency = results.count(value)
            frequencies += [frequency]
    print(frequencies, 'Mnogo')
else:   
    for roll_num in range(r_n):
        result = dice[0].roll()
        results += [result]
    print(results)

    for value in range(1, dice_sides[0] + 1):
        frequency = results.count(value)
        frequencies += [frequency]
    print(frequencies, 'Malo')



hist = pygal.Bar()
hist.title = "Резульаты n бросков m куба/ов d{}".format(dice_sides)
hist.title += "\n n = {}; m = {}".format(r_n, dice_numbers)
if dice_numbers > 1:
    if approval == 'y':
        for count in range(dice_numbers):
            maxresult = dice_numbers*dice_sides[count]
            hist.x_labels = list(range(dice_numbers, maxresult))
    else:
        maxresult = dice_numbers*dice_sides[0] + 1
        hist.x_labels = list(range(dice_numbers, maxresult))
else:
    hist.x_labels = list(range(dice_numbers, (dice_numbers*dice_sides[0]) + 1))
hist.x_title = 'Результы'
hist.y_title = 'Частота результатов'
hist.add('d{}'.format(dice_sides), frequencies)
hist.render_to_file('dice_visual.svg')