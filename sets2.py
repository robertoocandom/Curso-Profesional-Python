
import random

def remove_duplicated_of_list(list_with_duplicate):
    return list(set(list_with_duplicate))

def run():
    list_with_duplicate = []
    for _ in range(0, 25):
        numero = random.randint(0, 10)
        list_with_duplicate.append(numero)
    
    print(f'Lista Original {list_with_duplicate}')

    print("Lista sin Duplicados " + str(remove_duplicated_of_list(list_with_duplicate)))

if __name__ == '__main__':
    run()