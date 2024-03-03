year = {
    1: 31,
    2: 28,
    3: 31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}
up_year = {
    1: 31,
    2: 29,
    3: 31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}
one_mas = []
two_mas = []
for f in open("a0.txt"):
    count = 0
    one, two = f.split("\t")
    one_mas = list(map(int,one.split(".")))
    two_mas = list(map(int,two.split(".")))
    for i in range(one_mas[-1], two_mas[-1]):
        count += 366 if i % 4 == 0 else 365
    if one_mas[2] % 4 == two_mas[2] % 4:
        count -= 1

    while not(one_mas[0] == two_mas[0] and one_mas[1] == two_mas[1]):
        one_mas[0] = one_mas[0] + 1
        if up_year[one_mas[1]] < one_mas[0] and one_mas[2] % 4 == 0:
            one_mas[0] = 1
            one_mas[1] = one_mas[1] + 1
            if one_mas[1] > 12:
                one_mas[1] = 1
                one_mas[2] = one_mas[2] + 1
        if year[one_mas[1]] < one_mas[0] and one_mas[2] % 4 != 0:
            one_mas[0] = 1
            one_mas[1] = one_mas[1] + 1
            if one_mas[1] > 12:
                one_mas[1] = 1
                one_mas[2] = one_mas[2] + 1
        count += 1


    print(count)

