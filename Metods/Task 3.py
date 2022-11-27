class Add():
    def __init__(self, argument):
        self.argument = argument

    def __add__(self, other):
        return other + self.argument
a = Add(355)
l = Add(99)
e = a + l
print(e)