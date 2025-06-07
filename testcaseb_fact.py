# testB_fact_calc.py

def compute_factorial(x):
    # compute factorial of x
    if x <= 1:
        return 1
    return x * compute_factorial(x - 1)


if __name__ == "__main__":
    res = compute_factorial(5)
    print(res)
