class User():
    def sign_in(self):
        print('logged in')

    def __int__(self, email):
        self.email = email


class Wizard(User):
    def __int__(self, name, power, email):
        # the super() method
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attack with power of {self.power}")


class Archer(User):
    def __int__(self, name, num_arrows, email):
        # the super() method
        super().__init__(email)
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attack with arrows, number of arrows remaining are {self.num_arrows}')


class Hybrid(Wizard, Archer):
    def __init__(self, name, power, num_arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, num_arrows)


wizard1 = Wizard()
wizard1.name = 'Marlin'
wizard1.power = 50
wizard1.email = 'marlin@gmail.com'
archer1 = Archer()
archer1.name = 'Robin'
archer1.num_arrows = 100
archer1.email = 'archer@gmail.com'

hb1 = Hybrid()
hb1.name = 'Borgie'
hb1.power = 65
hb1.num_arrows = 150
print(hb1.num_arrows)
