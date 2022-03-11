import time

class FiboIter():
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter +=1
            return self.n1
        elif self.counter == 1:
            self.counter +=1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            if self.aux > maximo:
                print(f'Aqui esta tu serie fibonacci hasta el numero {maximo}' )
                raise StopIteration
            self.n1 = self.n2
            self.n2 = self.aux
            return self.aux

if __name__ == '__main__':
    maximo = int(input(f'Introduce un numero maximo de tu serie Fibonacci: '))
    fibonacci = FiboIter()
    for element in fibonacci:
        print(element)
        time.sleep(0.5)
            