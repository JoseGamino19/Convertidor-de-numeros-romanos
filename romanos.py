def romanos(s):
    if s == "I":
        return 1
    if s == "V":
        return 5
    if s == "X":
        return 10
    if s == "L":
        return 50
    if s == "C":
        return 100
    if s == "D":
        return 500
    if s == "M":
        return 1000
    return -1


def de_romano_a_decimal(romano):
    numero = 0
    i = 0

    while i < len(romano):
        x1 = romanos(romano[i])

        if i + 1 < len(romano):
            x2 = romanos(romano[i + 1])

            if x1 >= x2:
                numero = numero + x1
                i = i + 1
            else:
                numero = numero + x2 - x1
                i = i + 2

        else:
            numero = numero + x1
            i = i + 1

    return numero


x = 'XXIV'
print("El numero es ")
print(de_romano_a_decimal(x))