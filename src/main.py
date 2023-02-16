from tempfile import tempdir
from sklearn.tree import DecisionTreeRegressor


amount = 20
L = [n for n in range(amount)]
N = ['Adrian', 'Filip', 'Martin', 'Dominik', 'Jana', 'Lucia', 'Pavol']
D = []

squared_L = [n**2 for n in L]

def populate_dictionary(id_list: list[int], name_list: list[str]):
    for id in L:
        temp_dict = {'id': id, 'name': ''}
        D.append(temp_dict)
    for index, name in enumerate(N):
        D[index]['name'] = name

def print_list_items(list: list):
    for i in list:
        print(i)

def print_every_kth(list:list, start: int, end: int, step: int):
    for i in list[start:end:step]:
        print(i)

def main():
    pass
    
if __name__ == "__main__":
    print("Running main() function..")
    main()