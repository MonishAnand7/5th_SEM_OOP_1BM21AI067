calculate_area = lambda radius: 3.14159 * radius ** 2

def main():
    radius = float(input("Enter the radius of the circle: "))

    area = calculate_area(radius)

    print(f"The area of the circle with radius {radius} is: {area:.2f}")


if __name__ == "__main__":
    main()
