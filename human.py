class Human:
    def __init__(self):
        self.name = "Arif"
        self.head = self.Head()
    def display(self):
        print("Name is ", self.name)
        self.head.talk()
    class Head:
        def __init__(self):
            self.brain = self.Brain()
        def talk(self):
            print("Talking...")
            self.brain.think()
        class Brain:
            def think(self):
                print("Thinking...")

p = Human()
p.display()