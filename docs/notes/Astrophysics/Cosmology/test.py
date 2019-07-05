def main():
    answer = None

    # Check if answer is a float or integer

    while True:
        answer = input("Enter a value: ")
        try:
            float(answer)
        except ValueError:
            print("Your answer needs to be an integer or decimal")
            continue
        if float(answer) <= 0:
            print("Your answer needs to be positive")
            continue
        else:
            break

main()