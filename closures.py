# Roberto, 2 -> RobertoRoberto
# Caracas, 3 -> CaracasCaracasCaracas

def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "La cadena introdicida debe ser solo de caracteres"
        return string * n
    return repeater

# funcion para hacer divisiones

def make_division_by(n):
    def division(x):
        return x / n
    return division


def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))
    division_by_5 = make_division_by(5)
    print(division_by_5(100))
    division_by_18 = make_division_by(18)
    print(division_by_18(54))
if __name__ == '__main__':
    run()
