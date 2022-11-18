import pygal

from dice import Dice

dice_numbers = int(input('Введите количество кубиков: '))
dice_sides = int(input('Введите количество граней: '))
r_n = int(input('Введите количество бросков: '))

dice = []
results = []
frequencies = []

for d_c in range(1, dice_numbers+1):
    dice += [Dice(dice_sides)]

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

hist = pygal.Bar()
hist.title = "Резульаты n бросков m куба/ов d{}".format(dice[0].num_sides)
hist.title += "\n n = {}; m = {}".format(r_n, dice_numbers)
hist.x_labels = list(range(dice_numbers, (dice_numbers*dice_sides) + 1))
hist.x_title = 'Результы'
hist.y_title = 'Частота результатов'

hist.add('d{}'.format(dice_sides), frequencies)
hist.render_to_file('dice_visual.svg')

