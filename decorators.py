from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print('Pasaron ' + str(time_elapsed.total_seconds()) + ' Segundos')
    return wrapper 

@execution_time
def random_func():
    for _ in range(1, 1000000):
        pass
    return print('Termine el ciclo')
@execution_time
def sumando(a: int, b:int) -> int:
    for _ in range(1, 10000):
        pass
    suma = a +b
    return print(f'La suma es: {suma}')

@execution_time
def saludos_personal(nombre):
    for _ in range(1, 10000):
        pass
    return print(f'Hola {nombre}')

random_func()
sumando(5, 5)
saludos_personal('Roberto')

        
