class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'Name': 'Oyogo',
            'Occupation': 'Student',
        }

    def __str__(self):
        return f'The toy has a color of {self.color}, and an age of {self.age}'

    def __call__(self):
        return 'Hurray!!'

    def __getitem__(self, i):
        return self.my_dict[i]

action_figure = Toy('red', 0)
print(str(action_figure))
print(action_figure())
print(action_figure['Name'])
print(action_figure['Occupation'])