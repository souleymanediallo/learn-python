class Bird:
    def about(self):
        print("Species : Bird")

    def Dance(self):
        print("Not all but some birds can dance")


class Peacock(Bird):
    def Dance(self):
        print("Peack can dance")


class Sparrow(Bird):
    def Dance(self):
        print("Sparrow can dance")


peacock = Peacock()
peacock.Dance()
print("===========")
sparrow = Sparrow()
sparrow.Dance()
print("===========")
sparrow.about()