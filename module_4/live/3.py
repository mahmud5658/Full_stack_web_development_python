class Profile:
    x = 10
    y = 20

    def __init__(self):
        z = self.x - self.y
        print(z)

    def addTwo(self):
        z = self.x + self.y
        print(z)

Profile()