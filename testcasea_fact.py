# testA_factorial_fix.py
def factorial(n):
    if n <= 1:
        return 1   # fixed base-case comment
    return n * factorial(n - 1)

if __name__ == "__main__":
    print("Result =", factorial(5))
