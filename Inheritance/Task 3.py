
class SpaceObject:

    def __init__(self, size):
        self.size = size


class Star(SpaceObject):

    def __init__(self, size, brightness):
        super().__init__(size)
        self.brightness = brightness


    def shine(self):
        print(f": {self.brightness}")

    def size(self):
        print(f": {self.size}")


class Planet(SpaceObject):
    def __init__(self, size, population, growth):
        super().__init__(size)
        self.population = population
        self.growth = growth


    def population_in_years(self, years):
        print(f" {years} :{self.population + self.growth * years} ")

star = Star(100, 70)
star.shine()


planet = Planet(200, 500, 150)
planet.population_in_years(20)