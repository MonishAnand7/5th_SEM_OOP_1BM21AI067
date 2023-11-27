class Calculator:
    def __init__(self, version):
        self.version = version

    def display_version(self):
        print(f"Calculator Version: {self.version}")

    @staticmethod
    def add_numbers(num1, num2):
        return num1 + num2


def main():
    version1 = input("Enter version for Calculator 1: ")
    version2 = input("Enter version for Calculator 2: ")

    calculator1 = Calculator(version1)
    calculator2 = Calculator(version2)

    calculator1.display_version()
    calculator2.display_version()

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = Calculator.add_numbers(num1, num2)

    print(f"The sum of {num1} and {num2} is: {result}")


if __name__ == "__main__":
    main()
