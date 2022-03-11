import time

def fibo_gen():
    n1, n2 = 0, 1
    while True:
        yield n1
        n1, n2 = n2, n1+n2

if __name__ == '__main__':
    
    maximo = int(input("Introduce un numero maximo de tu serie Fibonacci:"))
    fibonacci = fibo_gen()
    for element in fibonacci:
        if element <= maximo:
            print(element)
            time.sleep(0.5)
        else:
             print("Aqui esta tu serie fibonacci hasta el numero "  + str(maximo) )
             break