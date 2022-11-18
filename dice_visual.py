import pygal

from dice import Dice

dice = Dice(20)

results = []
for roll_num in range(100):
    result = dice.roll()
    results += [result]

frequencies = []
for value in range(1, dice.num_sides +1):
    frequency = results.count(value)
    frequencies += [frequency]

hist = pygal.Bar()
hist.title = "Резульаты тысячи бросков одного куба d{}".format(dice.num_sides)
hist.x_labels = list(range(1, dice.num_sides +1))
hist.x_title = 'Результы'
hist.y_title = 'Частота результатов'

hist.add('d{}'.format(dice.num_sides), frequencies)
hist.render_to_file('dice_visual.svg')

print(frequencies)