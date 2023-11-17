class PlayerCharacter:

    friendship = True

    def __int__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

player1 = PlayerCharacter()
player1.name = "Brian"
player1.age = 23
player2 = PlayerCharacter()
player2.name = "Cindy"
player2.age = 20
print(f"{player1.name} is {player1.age} years old")
print(f"{player2.name} is {player2.age} years old")
print(player1.friendship)
print(player2.friendship)
