L = [1,2,4,6,3,7]

def sort(list: list):
    for i, v in enumerate(list):
        for j in range(len(list) -1 -i):
            if list[j] > list[j+1]:
                tmp = list[j]
                list[j] = list[j+1]
                list[j+1] = tmp
                
def main():
    print(L)
    sort(L)
    print(L)

if __name__ == "__main__":
    main()