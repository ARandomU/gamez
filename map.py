import enemies
from random import randint
locations = {
    1: 'corridor A',
    2: 'corridor B',
    3: 'corridor C',
    4: 'corridor D',
    5: 'corridor E',
    6: 'corridor F',
    7: 'corridor G',
    8: 'corridor H',
    9: 'corridor I',
    10: 'corridor J'}


class Map(object):
    def map(self, classe, level):
        self.classe = classe
        self.level = level
        maps = 5
        height = 0
        direct = """Left, Right, Up or Down?"""
        money = "To fight a Slime type slime."
        cash = "To fight a HobGoblin type hobgob."
        cheque = "To fight a Minotaur type minotaur"
        print(direct)
        print(money)
        print(cash)
        print(cheque)
        while True:
            check = locations[maps] + ' room ' + str(height)
            choice = input(">")
            if maps == 10:
                print('You have fallen off the world and landed in the center of the map.')
                height = 0
                maps = 5
            elif maps == 1:
                print('You have fallen off the world and landed in the center of the map.')
                height = 0
                maps = 5
            elif height == -6:
                print('You have fallen off the world and landed in the center of the map.')
                height = 0
                maps = 5
            elif height == 6:
                print('You have fallen off the world and landed in the center of the map.')
                height = 0
                maps = 5
            elif 'left' in choice:
                maps -= 1
                print(check)
            elif 'right' in choice:
                maps += 1
                print(check)
            elif 'up' in choice:
                height += 1
                print(check)
            elif 'down' in choice:
                height -= 1
                print(check)
            elif 'flee' in choice:
                print("you have fled to the center")
                height = 0
                maps = 5
            elif choice == 'slime':
                enemies.Slime(self.classe).slime(self.level)
            elif choice == 'hobgob':
                enemies.Hobgob(self.classe).hobgob(self.level)
            elif choice == 'minotaur':
                enemies.Minotaur(self.classe).minotaur(self.level)
            else:
                print('wut')


class Events(Map):
    chestknight = {1: 'cursed sword', 2: 'unbreakable boots',
                   3: 'unbreakable legging\'s', 4: 'unbreakable chestplate', 5: 'unbreakable helmet'}
    chestarcher = {1: 'blessed bow', 2: 'boots of thor',
                   3: 'leggings of thor', 4: 'chestplate of thor', 5: 'helmet of thor'}
    chestmage = {1: 'staff of Zeus', 2: 'boots of belle',
                 3: 'leggings of belle', 4: 'fashionable coat of belle', 5: 'white hair of belle'}
    chests = {1: 'chestknight', 2: 'chestarcher', 3: 'chestmage'}

    def chest(self):
        print('you have found a chest')
        if True:
            item = str(Events.chestknight[randint(1, 5)])
            print(f'you have found {item}')
