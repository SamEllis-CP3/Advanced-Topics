from csv import reader

class Dog:
    def __init__(self, number, name, bread):
        self.number = number
        self.name = name
        self.breed = bread
    def __str__(self):
        return f"Number: {self.number}\nName: {self.name}\nBreed: {self.breed}\n===============\n"

dogs = []

with open('Dogs.csv') as csv_file:
    csv_reader = reader(csv_file, delimiter=',')
    next(csv_reader)
    for number, name, bread in csv_reader:
        dogs.append(Dog(number, name, bread))

        
for dog in dogs:
    print(dog)