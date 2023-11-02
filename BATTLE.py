import random

class Soldier:

    def __init__(self, name='Noname', health = 100):
        self.name = name
        self.health = health

    def set_name(self, name):
        self.name = name

    def make_kick(self, enemy):
        enemy.health -= 20
        if enemy.health < 0:
            enemy.health = 0
        self.health += 10
        print(f'{self.name} ударил {enemy.name}')
        print(f'{enemy.name} = {enemy.health}')

class Battle:

    def __init__(self, solder1, solder2):
        self.solder1 = solder1
        self.solder2 = solder2
        self.result = 'Все только начинается'

    def battle(self):
        while self.solder1.health > 0 and self.solder2.health > 0:
            n = random.randint(1, 2)
            if n == 1:
                self.solder1.make_kick(self.solder2)
            else:
                self.solder2.make_kick(self.solder1)
        if self.solder1.health > self.solder2.health:
            self.result = self.solder1.name + '  *ПОБЕДИЛ*  '
        else:
            self.result = f'{self.solder2.name}  *ПОБЕДИЛ*  '

    def who_win(self):
        print((self.result))

first = Soldier('Mr. First', 140)
second = Soldier()
second.set_name('Mr.Second')
b = Battle(first, second)
b.battle()
b.who_win()

