def fibonacci(number):
    a, b = 0, 1
    while a < number:
        print(a, end=' ')
        a, b = b, a+b
    print()
    if a == number:
        return f"{number} belongs to Fibonacci sequence"
    else:
        return f"{number} it does not belong to the Fibonacci sequence"

def main():
    print("Type a number:")
    number = int(input())
    print(fibonacci(number))

if __name__ == "__main__":
    main()