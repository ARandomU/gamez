import map


class Character(object):
    def __init__(self, name):
        self.name = name

    def archer(self):
        print(f"{self.name} is an Archer.")
        vitality = 200
        health = vitality
        print(f'Your health is {health}.')
        print("""Bow and Arrow level 1, light armour level 1.
            Skills
                Shoot. level 1
                Doge.
                """)
        while True:
            select = input("Type ready to begin.")
            if select == 'ready':
                map.Map().map('archer', 1)
            else:
                print('wuut')

    def knight(self):
        print(f"{self.name} is a Knight.")
        vitality = 200
        health = vitality
        print(f'Your health is {health}.')
        print("""Sword level 1, heavy armour level 1.
            Skills
                Strike. level 1
                Parry. level 1
                Doge
                """)
        while True:
            select = input("Type ready to begin.")
            if select == 'ready':
                map.Map().map('knight', 1)
            else:
                print('wuut')

    def mage(self):
        print(f"{self.name} is a Mage.")
        vitality = 200
        health = vitality
        print(f'You health is {health}.')
        print("""Dope Robe level 1.
            Skills
                Fireball. level 1
                Shield. level 1
                Doge""")
        while True: 
            select = input("Type ready to begin.")
            if select == 'ready':
                map.Map().map('mage', 1)
            else:
                print('wuut')

    def start(self):
        print(f"Welcome {self.name}.")
        self.classes()

    def classes(self):
        print("""
        To view your stats type stats during combat
        Choose a class
        
        Archer: Bow and Arrow level 1, light armour level 1.
            Skills
                Shoot,
                Doge,
        Knight: Sword level 1, heavy armour level 1.
            Skills
                Strike
                Parry
                Doge
        Mage: Dope Robe level 1.
            Skills
                Fireball
                Shield
                Doge
        """)
        while True:
            choice = input()
            if choice == 'Archer':
                self.archer()
            elif choice == 'Knight':
                self.knight()
            elif choice == 'Mage':
                self.mage()
            else:
                print('wut')


def credit():
    credite = {
        1: 'Game Design: me',
        2: 'Class Design: me',
        3: 'Debugger: me',
        4: 'Game Engine: Me Myself an I by: me',
        5: 'Coding: me',
        6: 'Art: me',
        7: 'Concept Art: me',
        8: 'Production: me',
        9: 'Outsourcing: Google',
        10: 'Revisions: me',
        11: 'Prototype: me',
        12: 'Project Manager: me',
        13: 'Programming Staff: me',
        14: 'Art and Design Staff: me',
        15: 'Animation Staff: me',
        16: 'Human Resources: me',
        17: 'Ceo: me'
    }

    for i in range(1, 18):
        print(credite[i])


ed = input("name? \n")
fred = Character(ed)
fred.start()
