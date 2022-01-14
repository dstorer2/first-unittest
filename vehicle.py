class Vehicle:

    tune_up_amt = 15

    def __init__(self, color, sound, numDoors, type, topSpeed):
        self.color = color
        self.sound = sound
        self.numDoors = numDoors
        self.type = type
        self.topSpeed = topSpeed
    
    def makeSound(self):
        print(self.sound)

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.color, self.sound)
    
    @property
    def full_deets(self):
        return '{} {}-door {}'.format(self.color, self.numDoors, self.type)

    def give_tune_up(self):
        self.topSpeed = self.topSpeed + self.tune_up_amt