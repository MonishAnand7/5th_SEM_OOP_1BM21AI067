def get_numbers_from_user():
    numbers = input("Enter a set of numbers separated by spaces: ")
    numbers_list = [int(num) for num in numbers.split()]
    return numbers_list

def find_largest_number(numbers):
    if not numbers:
        return None  # Return None if the list is empty
    else:
        largest_number = numbers[0]
        for number in numbers:
            if number > largest_number:
                largest_number = number
        return largest_number

def main():
    numbers = get_numbers_from_user()
    largest_number = find_largest_number(numbers)

    if largest_number is not None:
        print(f"The largest number is: {largest_number}")
    else:
        print("No numbers provided.")

if __name__ == "__main__":
    main()
