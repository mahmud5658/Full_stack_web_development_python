class Father:
    x = 20
    y = 30

    def __init__(self):
        z = self.x + self.y
        print(z)

    @staticmethod
    def mulTwo():
        z = Father.x * Father.y
        print(z)

    def addTwo(self):
        z = self.x + self.y
        print(z)


class Son(Father):
   pass


Father()
Son()