from calculator import Calculator

def main():
    num_1 = int(input("Please enter the first number: "))
    num_2 = int(input("Please enter the second number: "))
    action = input("Please enter the action. Choose from add, sub, mul, div: ")
    answer = Calculator._input(num_1, num_2, action)
    print(answer)

main()
