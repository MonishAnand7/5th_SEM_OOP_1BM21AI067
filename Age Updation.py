class BirthdayBoy:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Birthday(self):
        self.age += 1

name_input = input("Enter the name of the birthday boy: ")
age_input = int(input("Enter the age of the birthday boy: "))

birthday_boy_instance = BirthdayBoy(name_input, age_input)

birthday_boy_instance.Birthday()

print(f"{birthday_boy_instance.name}'s age after the birthday: {birthday_boy_instance.age}")
