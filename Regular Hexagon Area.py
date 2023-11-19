import math

def HexagonArea(side_length):
    if side_length <= 0:
        return "Invalid input. Side length must be greater than zero."
    
    area = (3 * math.sqrt(3) * side_length ** 2) / 2
    return area

user_input = float(input("Enter the length of a side of the regular hexagon: "))
hexagon_area = HexagonArea(user_input)

print(f"The area of the regular hexagon with side length {user_input} is: {hexagon_area}")
