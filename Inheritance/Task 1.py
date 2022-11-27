class Hero:
    def __init__(self, health, power):
        self.health = health
        self.power = power


class Magician(Hero):
    def __init__(self, health, power):
        super().__init__(health, power)

    def hello(self):
        print('')

    def attack(self, another_gamer):
        another_gamer.health -= self.power * 4
        self.power -= 5
        print('!')



hero = Hero(100, 10)
mag = Magician(100, 10)
mag.hello()
mag.attack(hero)
print(f': {mag.power}')
print(f'hero: {hero.health}')