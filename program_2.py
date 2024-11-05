# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).
import random

def main():
    try:
        numbers = int(input("How many random numbers do you want the file to hold (up to 1,000)? "))
        if numbers < 1 or numbers > 1000:
            print("The number must be between 1 and 1000. Try again please 😔😔")
            return
        else:
            with open('randomNumbersGenerated.txt', 'w') as file:
                for r in range(numbers):
                    RandomNumber = random.randint(1,500)
                    file.write(f'{RandomNumber}\n')

            print(f'{numbers} random numbers have been added to the file.')
    except ValueError:
        print("No. That is not an integer. TRY AGAIN 😒")

if __name__ == "__main__":
    main()

