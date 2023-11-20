from datetime import datetime

class Dog:
    def __init__(self, name, size, breed='unknown', dob='unknown'):
        self.SetName(name)
        self.size = size
        self.breed = breed
        self.SetDOB(dob)

    def Bark(self):
        print(f"{self.name} says: Woof! Woof!")

    def SetName(self, name):
        if 2 <= len(name) <= 30 and name.isalpha():
            self.name = name.title()
        else:
            print("Invalid name. Please enter a name with 2-30 alphabetical characters.")

    def SetDOB(self, dob):
        try:
            date_object = datetime.strptime(dob, '%d/%m/%Y')
            self.dob = date_object.strftime('%d/%m/%Y')
        except ValueError:
            print("Invalid date format. Please use DD/MM/YYYY.")

    def Age(self):
        if self.dob != 'unknown':
            today = datetime.now()
            birth_date = datetime.strptime(self.dob, '%d/%m/%Y')
            age_in_years = (today - birth_date).days / 365
            age_in_dog_years = age_in_years * 7
            return round(age_in_dog_years)
        else:
            print("Unknown Date of Birth. Age calculation not possible.")

name_input = input("Enter the dog's name: ")
size_input = input("Enter the dog's size: ")
breed_input = input("Enter the dog's breed (or press Enter for 'unknown'): ")
dob_input = input("Enter the dog's Date of Birth in DD/MM/YYYY format (or press Enter for 'unknown'): ")

my_dog = Dog(name_input, size_input, breed_input, dob_input)

my_dog.Bark()
print(f"{my_dog.name}'s age in dog years: {my_dog.Age()} years")
