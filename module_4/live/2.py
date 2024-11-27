class Profile:
    x = 2
    y = 30

    @staticmethod
    def addTwo():
        z = Profile.x + Profile.y
        print(z)


Profile.addTwo()
