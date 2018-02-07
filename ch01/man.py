class Man(object):
    def __init__(self, name):
        self.name = name
        print("Initialized!")

    def hello(self):
        print("hello {}!".format(self.name))

    def goodbye(self):
        print("Good-bye {}!".format(self.name))


m = Man("David")
m.hello()
m.goodbye()
