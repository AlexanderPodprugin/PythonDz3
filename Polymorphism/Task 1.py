class People():
    def quack(self):
        print("")


    def clothes(self):
        print("")


class Duck(People):
    def quack(self):
        print("")


    def clothes(self):
        print("")

a = People()
b = Duck()
ab = [a, b]
for i in ab:
    i.quack()
    i.clothes()