from random import randrange

def qs(collection: list) -> list:
    if len(collection) < 2:
        return collection

    # select random element as pivot
    pivot_idx = randrange(len(collection))
    pivot = collection[pivot_idx]

    left_side: list[int] = []
    right_side: list[int] = []

    for element in collection[:pivot_idx]:
        (right_side if element > pivot else left_side).append(element)

    for element in collection[pivot_idx + 1:]:
        (right_side if element > pivot else left_side).append(element)
    
    return qs(left_side) + [pivot] + qs(right_side)

def main():

    input = [1,666,6,420,3,69,8,88,9]
    output = qs(input)

    print(output)

if __name__ == "__main__":
    main()