class Parrot:
    def __int__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

parrot1 = Parrot()
parrot1.name = "Blu"
parrot1.age = 10
parrot2 = Parrot()
parrot2.name = "Woo"
parrot2.age = 15
parrot3 = Parrot()
parrot3.name = "Muu"
parrot3.age = 5

# print(parrot1)
# print(parrot2)
# print(parrot3)

print(f"{parrot1.name} is {parrot1.age} years old")
print(f"{parrot2.name} is {parrot2.age} years old")
print(f"{parrot3.name} is {parrot3.age} years old")