from sys import stdin
def table(nb, max=10):
    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1

if __name__ == "__main__":
    table(4)
    stdin.read(1)