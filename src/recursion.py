def recurse(n):
    if n == 1:
        return 1

    return n + recurse(n -1)

def main():
    print(recurse(5))

if __name__ == "__main__":
    main()