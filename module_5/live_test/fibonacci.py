def fibonacci_by_terms(n):
    if n <= 0:
        return []
    series = [0, 1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series[:n]

def fibonacci_by_max_value(max_value):
    if max_value < 0:
        return []
    series = [0, 1]
    while series[-1] + series[-2] <= max_value:
        series.append(series[-1] + series[-2])
    return series if max_value >= 1 else [0]

def input_checker(input_value):
    try:
        value = int(input_value)
        return value >= 0
    except ValueError:
        return False

def main():
    while True:
        print("\nChoose an option:")
        print("1. Generate Fibonacci series by number of terms")
        print("2. Generate Fibonacci series by maximum value")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            terms = input("Enter the number of terms: ")
            if input_checker(terms):
                terms = int(terms)
                result = fibonacci_by_terms(terms)
                print(f"Fibonacci series ({terms} terms): {', '.join(map(str, result))}")
            else:
                print("Invalid input. Please enter a non-negative integer.")

        elif choice == "2":
            max_value = input("Enter the maximum value: ")
            if input_checker(max_value):
                max_value = int(max_value)
                result = fibonacci_by_max_value(max_value)
                print(f"Fibonacci series (up to {max_value}): {', '.join(map(str, result))}")
            else:
                print("Invalid input. Please enter a non-negative integer.")

        elif choice == "3":
            print("Goodluck!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()