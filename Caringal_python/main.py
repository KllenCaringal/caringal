from project.ProbOne import probOne
from project.ProbTwo import probTwo
from project.ProbThree import probThree
from project.ProbFour import probFour
from project.ProbFive import probFive
from project.divider import divider

def main():
    print("Select a problem to solve (1-5):")
    print("1: Problem One")
    print("2: Problem Two")
    print("3: Problem Three")
    print("4: Problem Four")
    print("5: Problem Five")
    print()

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice < 1 or choice > 5:
                raise ValueError("Choice must be between 1 and 5.")
            divider()
            break
        except ValueError as ve:
            print(f"Invalid input: {ve}. Please enter an integer between 1 and 5.")
            divider()

    if choice == 1:
        probOne()
    elif choice == 2:
        probTwo()
    elif choice == 3:
        probThree()
    elif choice == 4:
        probFour()
    elif choice == 5:
        probFive()

if __name__ == "__main__":
    main()
