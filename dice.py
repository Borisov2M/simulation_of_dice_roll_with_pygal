import os
import time

from random import randint

class Dice():
    # Класс кубика
    def __init__(self, num_sides = 6):
        self.num_sides = num_sides
    
    def roll(self):
        return randint(1, self.num_sides)

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