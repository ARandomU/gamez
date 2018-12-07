from random import randint
from leveling import *


class Enemies(object):
    attacks = {1: 'punch',
               2: 'kick',
               3: 'charge',
               4: 'block',
               5: 'flee'
               }


class Combat(Enemies):
    levels = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five'
    }

    def combat(self, name, health, level, classe, mhealth):
        self.classe = classe
        self.name = name
        self.health = health
        self.mhealth = mhealth
        self.level = level
        attack = Enemies.attacks[randint(1, 4)]
        while health > 0 and mhealth > 0:
            seet = randint(0, 1)
            print(f'you run into a wild {self.name}')
            if seet == 0:
                print(f"The {self.name} tries to {attack} you.")
                print('What do you do?')
                move = input('>')
                if self.classe == 'archer':
                    if move == 'shoot':
                        print(f'The {self.name} hit\'s you before you can react')
                        health -= 100
                        print(f'Minus 100 health current health at {self.health}')
                        print(f"The {name}'s heath is at {mhealth}.")
                    elif move == 'doge':
                        print('you are partially damaged')
                        self.health -= 20
                    else:
                        print('wut')
                elif self.classe == 'knight':
                    if move == 'strike':
                        print(f'You try to strike the {self.name} but it hit\'s you')
                        health -= 100
                        print(f'Minus 100 health current health at {self.health}')
                        print(f"The {name}'s heath is at {mhealth}.")
                    elif move == 'parry':
                        print('You parry the hit')
                    elif move == 'doge':
                        print('you are partially damaged')
                        self.health -= 20
                    else:
                        print('wut')
                elif self.classe == 'mage':
                    if move == 'fireball':
                        print(f'the {self.name} doges your fireball and strikes you.')
                        health -= 100
                        print(f'Minus 100 health current health at {self.health}')
                        print(f"The {name}'s heath is at {mhealth}.")
                    elif move == 'shield':
                        print(f'You cast a shield and the {self.name} fails to hit you')
                    elif move == 'doge':
                        print('you are partially damaged')
                        self.health -= 20
                    else:
                        print('wut')
            elif seet == 1:
                print('What do you do?')
                move = input('>')
                if self.classe == 'archer':
                    if Levelling('archer', 1) and move == 'shoot':
                        print('You draw your bow and launch an arrow at the monster')
                        print(f'The monsters health is now {mhealth}.')
                        print(f'Your current health is {health}.')
                        mhealth -= randint(10, 50)
                    elif Levelling('archer', 2) and move == 'shoot':
                        print('You draw your bow and launch an arrow at the monster')
                        mhealth -= randint(50, 90)
                        print(f'the monsters health is now {mhealth}.')
                        print(f'Your current health is {health}.')
                    elif Levelling('archer', 3) and move == 'shoot':
                        print('You draw your bow and launch an arrow at the monster')
                        print(f'the monsters health is now {mhealth}.')
                        mhealth -= randint(90, 125)
                    elif Levelling('archer', 4) and move == 'shoot':
                        print('You draw your bow and launch an arrow at the monster')
                        print(f'the monsters health is now {mhealth}.')
                        mhealth -= randint(125, 150)
                    elif Levelling('archer', 5) and move == 'shoot':
                        print('You draw your bow and launch an arrow at the monster')
                        print(f'the monsters health is now {mhealth}.')
                        mhealth -= randint(150, 250)
                    elif move == 'doge':
                        print('you are partially damaged')
                        health -= 20
                elif self.classe == 'knight':
                    if Levelling(self.classe, 1) and move == 'strike':
                        print('You strike the monster with your sword.')
                        print(f'the monsters health is now {mhealth}.')
                        mhealth -= randint(20, 40)
                    elif Levelling(self.classe, 2) and move == 'strike':
                        print('You strike the monster with your sword.')
                        print(f'the monsters health is now {mhealth}.')
                        mhealth -= randint(40, 60)
                    elif Levelling(self.classe, 3) and move == 'strike':
                        print('You strike the monster with your sword.')
                        print(f'the monsters health is now {mhealth}.')
                        mhealth -= randint(60, 80)
                    elif Levelling(self.classe, 4) and move == 'strike':
                        print('You strike the monster with your sword.')
                        print(f'the monsters health is now {mhealth}.')
                        mhealth -= randint(80, 100)
                    elif Levelling(self.classe, 5) and move == 'strike':
                        print('You strike the monster with your sword.')
                        print(f'the monsters health is now {mhealth}.')
                        mhealth -= randint(100, 150)
                    elif move == 'parry':
                        print('You doge all damage.')
                    elif move == 'doge':
                        print('you are partially damaged')
                        health -= 20
                elif self.classe == 'mage':
                    print('mage')
                    if Levelling(self.classe, 1) and move == 'fireball':
                        print('You cast a mighty fireball.')
                        mhealth -= randint(50, 100)
                        print(f'The monsters health is now at {mhealth}')
                    elif Levelling(self.classe, 2) and move == 'fireball':
                        print('You cast a mighty fireball.')
                        mhealth -= randint(100, 150)
                        print(f'The monsters health is now at {mhealth}')
                    elif Levelling(self.classe, 3) and move == 'fireball':
                        print('You cast a mighty fireball.')
                        mhealth -= randint(150, 200)
                        print(f'The monsters health is now at {mhealth}')
                    elif Levelling(self.classe, 4) and move == 'fireball':
                        print('You cast a mighty fireball.')
                        mhealth -= randint(200, 250)
                        print(f'The monsters health is now at {mhealth}')
                    elif Levelling(self.classe, 5) and move == 'fireball':
                        print('You cast a mighty fireball.')
                        mhealth -= randint(250, 500)
                        print(f'The monsters health is now at {mhealth}')
                    elif Levelling(self.classe, 1) and move == 'shield':
                        print('You cast a shield and deflect the damage.')
                        mhealth -= randint(25, 100)
                        print(f'The monsters health is now at {mhealth}')
                    elif Levelling(self.classe, 2) and move == 'shield':
                        print('You cast a shield and deflect the damage.')
                        mhealth -= randint(50, 200)
                        print(f'The monsters health is now at {mhealth}')
                    elif Levelling(self.classe, 3) and move == 'shield':
                        print('You cast a shield and deflect the damage.')
                        mhealth -= randint(75, 300)
                        print(f'The monsters health is now at {mhealth}')
                    elif Levelling(self.classe, 4) and move == 'shield':
                        print('You cast a shield and deflect the damage.')
                        mhealth -= randint(100, 400)
                        print(f'The monsters health is now at {mhealth}')
                    elif Levelling(self.classe, 5) and move == 'shield':
                        print('You cast a shield and deflect the damage.')
                        mhealth -= randint(125, 500)
                        print(f'The monsters health is now at {mhealth}')
                    elif move == 'doge':
                        print('you are partially damaged')
                        health -= 20
                    else:
                        print('wut')
                elif move == 'stats':
                    print(f'Your weapon is level {self.level}.')
                    print(f'Your Armour is level {self.level}.')
                    print(f'Your skills are level {self.level}.')
            elif health > 0:
                Death().death()
            elif mhealth > 0:
                print('You win')


class Death(Enemies):

    memes = [
        'You would have kicked the bucket but you missed it tripped and died.',
        'You were going to sleep with the fishies but they did\'nt want you.',
        'Look at the sky and you will not be there cuz ur ded',
        'Running out of ideas so I\'m just gonna type this ur ded',
        'There once was a man and he died. You were the man.',
        'One Punch Man is the best, not that that concerns you ur dead',
        'A Quote directly from the mouth of JFK "Pay to win is how I became president."'
    ]

    def death(self):
        print(Death.memes[randint(0, 6)])
        return 'Character(ed).start()'


class Minotaur(Enemies):

    def __init__(self, classe):
        self.classe = classe

    def minotaur(self, level):
        self.level = level
        name = 'Minotaur'
        health = 600
        Combat().combat(name, 200, self.level, self.classe, health)

    def drops(self):
        drop = self.level
        drop += 1
        Levelling(self.classe, drop)


class Ogre(Enemies):

    def __init__(self, classe):
        self.classe = classe

    def ogre(self, level):
        self.level = level
        name = 'Ogre'
        health = 250
        Combat().combat(name, 200, self.level, self.classe, health)

    def drops(self):
        drop = self.level
        drop += 3
        Levelling(self.classe, drop)


class Hobgob(Enemies):
    def __init__(self, classe):
        self.classe = classe

    def hobgob(self, level):
        self.level = level
        name = 'Hobgob'
        health = 100
        Combat().combat(name, 200, self.level, self.classe, health)

    def drops(self):
        drop = self.level
        drop += 2
        Levelling(self.classe, drop)


class Slime(Enemies):
    def __init__(self, classe):
        self.classe = classe

    def slime(self, level):
        self.level = level
        name = 'slime'
        health = 20
        Combat().combat(name, 200, self.level, self.classe, health)

    def drops(self):
        drop = self.level
        drop += 1
        Levelling(self.classe, drop)
