def calculate_powers(base, limit):
    print("\nHere are the results:")
    for i in range(1, limit + 1):
        result = base ** i
        print(f"{base}^{i} = {result}")

def main():
    print("Welcome to Vrisha's Power Calculator! 🔢")
    
    while True:
        try:
            base = float(input("Enter the base number: "))
            limit = int(input("How many powers do you want to calculate? "))
            
            if limit < 1:
                print("Please enter a positive integer for the limit.")
                continue

            calculate_powers(base, limit)

            again = input("\nWould you like to try another number? (yes/no): ").strip().lower()
            if again != 'yes':
                print("Thanks for using Vrisha's Power Calculator! 😊")
                break

        except ValueError:
            print("Oops! Please enter valid numbers.")

if __name__ == "__main__":
    main()