import numpy as np

def random_walk_probability(p, q, endup, endown, start):
    positions = list(range(endown, endup + 1))
    n = len(positions)

    # Initialize coefficient matrix A and vector B
    A = np.zeros((n, n))
    B = np.zeros(n)

    # Boundary conditions
    A[0, 0] = 1
    B[0] = 0
    A[-1, -1] = 1
    B[-1] = 1


    for i in range(1, n - 1):
        A[i, i - 1] = -q
        A[i, i] = 1
        A[i, i + 1] = -p
        B[i] = 0
    

    # Solve the linear system
    X = np.linalg.solve(A, B)

    # Get the probability starting from 'start'
    idx = positions.index(start)
    return X, idx

def og_random_walk(p, q, endup, endown, start):
    """
    This was my initial idea, but doesnt work in the code space. Cant seem to solve a system of linear equations effectively using recursion
    This has the thoery more intuitively but not possible to run code (overly recursive)
    """

    # Base Cases
    if start == endup:
        return 1
    if start == endown:
        return 0

    # Recursive Calls with Memoization
    P_up1 = og_random_walk(p, q, endup, endown, start + 1)
    P_down1 = og_random_walk(p, q, endup, endown, start - 1)

    P_start = p * P_up1 + q * P_down1
    return P_start

def formulaic_random_walk(p, q, endup, endown, start, memo=None):
    if p != q:
        denom = (q / p) ** endup - (q / p) ** endown
        num = (q / p) ** start - (q / p) ** endown
    else:
        num = start - endown
        denom = endup - endown
    
    return num / denom


def main():
    start = 100
    endup = 10000
    endown = 0
    p_up = 0.51
    p_down = 1 - p_up

    # The probability of reaching 10000 before 0 starting from 10 is: 0.3297157119850198
    # The probability of reaching 10000 before 0 starting from 100 is: 0.9816941291599397
    # (Interesting LOL) ^ with 0.51 advance probability

    X, idx = random_walk_probability(p_up, p_down, endup, endown, start)
    probability = X[idx]
    # print([i for i in X], "\n\n")
    print(f"The probability of reaching {endup} before {endown} starting from {start} is: {probability}\n")

    probability = formulaic_random_walk(p_up, p_down, endup, endown, start)
    print(f"(Using Formula to Check) The probability of reaching {endup} before {endown} starting from {start} is: {probability}")

if __name__ == "__main__":
    main()
