def is_repdigit(N):
    N_str = str(N)
    return all(digit == N_str[0] for digit in N_str)
N = input()

if is_repdigit(N):
    print("true")
else:
    print("false")
