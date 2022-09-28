def zero_division():
    return 5 / 0


def main():
    try:
        zero_division()
    except ZeroDivisionError:
        print("Cannot divide by Zero")


if __name__ == "__main__":
    main()
