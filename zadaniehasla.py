with open("hasla.txt", "r") as file:
    hasla = [line.strip() for line in file.readlines()]
    
    # Zadanie 4a
    with open("wynik4a.txt", "w") as result:
        result.write(f'Hasla z parzysta liczba znakow: {len([line for line in hasla if len(line)%2 == 0])}\nHasla z nieparzysta liczba znakow: {len([line for line in hasla if len(line)%2 == 1])}')

    # Zadanie 4b
    with open("wynik4b.txt", "w") as result:
        [result.write(f"{line}\n") for line in hasla if line == line[::-1]]

    # Zadanie 4c
    with open("wynik4c.txt", "w") as result: