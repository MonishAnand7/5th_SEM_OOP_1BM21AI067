import math

class Number:
    def __init__(self, value):
        self.value = float(value)

    def isZero(self):
        return self.value == 0

    def isPositive(self):
        return self.value > 0

    def isNegative(self):
        return self.value < 0

    def isOdd(self):
        return self.value % 2 != 0

    def isPrime(self):
        if self.value < 2:
            return False
        for i in range(2, int(math.sqrt(self.value)) + 1):
            if self.value % i == 0:
                return False
        return True

    def isArmstrong(self):
        temp = self.value
        n = len(str(temp))
        total = 0
        while temp > 0:
            digit = temp % 10
            total += digit ** n
            temp //= 10
        return total == self.value

    def getFactorial(self):
        if self.value < 0:
            return None
        if self.value == 0:
            return 1
        factorial = 1
        for i in range(1, int(self.value) + 1):
            factorial *= i
        return factorial

    def getSqrt(self):
        if self.value < 0:
            return None
        return math.sqrt(self.value)

    def sumDigits(self):
        total = 0
        temp = abs(int(self.value))
        while temp > 0:
            total += temp % 10
            temp //= 10
        return total

    def getReverse(self):
        sign = -1 if self.value < 0 else 1
        reverse = int(str(abs(int(self.value)))[::-1])
        return sign * reverse

def main():
    value = float(input("Enter a number: "))

    num = Number(value)

    print(f"isZero: {num.isZero()}")
    print(f"isPositive: {num.isPositive()}")
    print(f"isNegative: {num.isNegative()}")
    print(f"isOdd: {num.isOdd()}")
    print(f"isPrime: {num.isPrime()}")
    print(f"isArmstrong: {num.isArmstrong()}")
    print(f"getFactorial: {num.getFactorial()}")
    print(f"getSqrt: {num.getSqrt()}")
    print(f"sumDigits: {num.sumDigits()}")
    print(f"getReverse: {num.getReverse()}")

if __name__ == "__main__":
    main()
