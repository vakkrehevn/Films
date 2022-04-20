import pickle
import random
from datetime import datetime
from threading import Timer


def Se(H):
    for i in range(len(H)):
        t = TaskManager()
        if int(t) > (int(H[i].T1[0]) + int(H[i].ti) // 60):
            print(H[i].T1[0] + ":00 сеанс прошёл")
        elif int(H[i].T1[0]) <= int(t) <= (int(H[i].T1[0]) + int(H[i].ti) // 60):
            print(H[i].T1[0] + ":00 сеанс идет")
        else:
            print(H[i].T1[0] + ":00")

        if int(t) > (int(H[i].T2[0]) + int(H[i].ti) // 60):
            print(H[i].T2[0] + ":00 сеанс прошёл")
        elif int(H[i].T2[0]) <= int(t) <= (int(H[i].T2[0]) + int(H[i].ti) // 60):
            print(H[i].T2[0] + ":00 сеанс идет")
        else:
            print(H[i].T2[0] + ":00")

        if int(t) > (int(H[i].T3[0]) + int(H[i].ti) // 60):
            print(H[i].T3[0] + ":00 сеанс прошёл")
        elif int(H[i].T3[0]) <= int(t) <= (int(H[i].T3[0]) + int(H[i].ti) // 60):
            print(H[i].T3[0] + ":00 сеанс идет")
        else:
            print(H[i].T3[0] + ":00")


def Zal():
    rows = 3
    cols = 3
    tab = [[0] * cols for _ in range(rows)]
    index = 0
    for row in range(rows):
        for col in range(0, cols, +1):
            index += 1
            tab[row][col] = index
    return tab


def Izal(tab, N):
    if N<=0:
        return tab
    else:
        n = int(input("Выберите место: "))
        for i in range(len(tab)):
            for j in range(len(tab[i])):
                if tab[i][j] == n:
                    tab[i][j] = "x"
                    return Izal(tab, N-1)


def Pzal(tab):
    for row in tab:
        print('\t'.join(map(str, row)))
    print("  экран")


def Sorted1():
    print("если вы хотите отсортировать по убыванию введите 'IN' ,если по возрастанию ,то 'DE'.  ")
    u = input()
    for i in range(len(A)):
        vj = A[i].Eval
        A[i].vj = vj

    if u == 'IN':
        Arr = sorted(A, key=lambda x: x.vj, reverse=True)
    if u == 'DE':
        Arr = sorted(A, key=lambda x: x.vj)
    for i in range(d):
        print(Arr[i].Name, Arr[i].Director, Arr[i].Country, Arr[i].Date, Arr[i].Eval)


def Sorted2():
    for i in range(len(A)):
        vj = A[i].Name
        A[i].vj = vj

    Arr = sorted(A, key=lambda x: x.vj)
    for i in range(d):
        print(Arr[i].Name, Arr[i].Director, Arr[i].Country, Arr[i].Date, Arr[i].Eval)


def Sorted3():
    print("если вы хотите отсортировать по убыванию введите 'IN' ,если по возрастанию ,то 'DE'.  ")
    u = input()
    for i in range(len(A)):
        vj = A[i].Date
        A[i].vj = vj

    if u == 'IN':
        Arr = sorted(A, key=lambda x: x.vj, reverse=True)
    if u == 'DE':
        Arr = sorted(A, key=lambda x: x.vj)
    for i in range(d):
        print(Arr[i].Name, Arr[i].Director, Arr[i].Country, Arr[i].Date, Arr[i].Eval)


def Con(A, S):
    for i in range(len(A)):
        if str(A[i].Country) == S:
            print(A[i].Country, A[i].Name, A[i].Director, A[i].Date, A[i].Eval)


class Films:
    Key = None
    Name = None
    Eval = None
    Date = None
    Time = None
    Country = None
    Director = None


class FF1:
    key = None
    name = None
    ti = None
    T1 = []
    T2 = []
    T3 = []


class F2:
    key = None
    name = None
    ti = None
    T1 = []
    T2 = []
    T3 = []


class F3:
    key = None
    name = None
    ti = None
    T1 = []
    T2 = []
    T3 = []


F1 = open("film.txt", "r", encoding='utf-8')
A = []
d = 0
while True:
    re = F1.readline()
    if not re:
        break
    d += 1
    re = re.split('"')
    a = Films()
    a.Key = re[0]
    a.Name = re[1]
    re2 = re[2]
    ind1 = re2.index('(')
    ind2 = re2.index(')')
    a.Director = re2[ind1 + 1:ind2]
    re2 = re2[:ind1] + re2[ind2 + 1:]
    re2 = re2.split(' ')
    a.Eval = re2[1]
    a.Date = re2[2]
    a.Time = re2[3]
    a.Country = re2[4]
    A.append(a)


def TaskManager():
    a = datetime.now().strftime("%H")
    t = Timer(1, TaskManager)
    t.start()
    return a


# , %H:%M:%S

F1 = open("film.dat", "wb")  # пишем в бинарное разрешение DAT
pickle.dump(A, F1)  # записываем массив А в бинарный файл
F1.close()
F1 = open("film.dat", "rb")  # что бы можно было считать
A = pickle.load(F1)
H1 = H2 = H3 = []

r = list(range(1, 25))
random.shuffle(r)
for i in range(1, 4):
    if i == 1:
        H1 = []
        h = FF1()
        h.key = r[i]
        h.T1.append("10")
        z1 = Zal()
        h.T1.append(z1)
        h.T2.append("15")
        z2 = Zal()
        h.T2.append(z2)
        h.T3.append("21")
        z3 = Zal()
        h.T3.append(z3)
        h.name = A[r[i] + 1].Name
        h.ti = A[r[i] + 1].Time
        H1.append(h)
    if i == 2:
        H2 = []
        h = F2()
        h.key = r[i]
        h.T1.append("10")
        z1 = Zal()
        h.T1.append(z1)
        h.T2.append("15")
        z2 = Zal()
        h.T2.append(z2)
        h.T3.append("21")
        z3 = Zal()
        h.T3.append(z3)
        h.name = A[r[i] + 1].Name
        h.ti = A[r[i] + 1].Time
        H2.append(h)

    if i == 3:
        H3 = []
        h = F3()
        h.key = r[i]
        h.T1.append("10")
        z1 = Zal()
        h.T1.append(z1)
        h.T2.append("15")
        z2 = Zal()
        h.T2.append(z2)
        h.T3.append("21")
        z3 = Zal()
        h.T3.append(z3)
        h.name = A[r[i] + 1].Name
        h.ti = A[r[i] + 1].Time
        H3.append(h)

print("Добро пожаловать в онлайн наш кинотеатр!")
while True:
    print("Выбрав цифру 1 вы можете забронировать место на одном из 3 сеансов")
    print("Выбрав цифру 2 вы можете посмотреть весь представленный ассортимент фильмов")
    print("Выбрав цифру 3 вы можете посмотреть список фильмов конкретной страны")
    n = int(input("Ваш выбор: "))
    if n == 1:
        f1 = f2 = f3 = ''
        print("АФИША: ")
        for i in range(len(H1)):
            f1 = H1[i].name
            print("   ", H1[i].name)
        for i in range(len(H2)):
            f2 = H2[i].name
            print("   ", H2[i].name)
        for i in range(len(H3)):
            f3 = H3[i].name
            print("   ", H3[i].name)
        print()
        f = input("Введите фильм: ")
        if f == f1:
            Se(H1)
            P1 = P2 = P3 = []
            x = input("Выберите время: ")
            for i in range(len(H1)):
                P1 = H1[i].T1
                P2 = H1[i].T2
                P3 = H1[i].T3
            if x == "1":
                tab = P1[1]
                Pzal(tab)
                n = int(input("Сколько мест вы хотите забронировать: "))
                tab = Izal(tab, n)
                Pzal(tab)
                print("Приятного просмотра!")
            if x == "2":
                tab = P2[1]
                Pzal(tab)
                n = int(input("Сколько мест вы хотите забронировать: "))
                tab = Izal(tab, n)
                Pzal(tab)
                print("Приятного просмотра!")
            if x == "3":
                tab = P3[1]
                Pzal(tab)
                n = int(input("Сколько мест вы хотите забронировать: "))
                tab = Izal(tab, n)
                Pzal(tab)
                print("Приятного просмотра!")
        elif f == f2:
            Se(H2)
            x = input("Выберите время: ")
            for i in range(len(H2)):
                P1 = H2[i].T1
                P2 = H2[i].T2
                P3 = H2[i].T3
            if x == "1":
                tab = P1[1]
                Pzal(tab)
                n = int(input("Сколько мест вы хотите забронировать: "))
                tab = Izal(tab, n)
                Pzal(tab)
                print("Приятного просмотра!")
            if x == "2":
                tab = P2[1]
                Pzal(tab)
                n = int(input("Сколько мест вы хотите забронировать: "))
                tab = Izal(tab, n)
                Pzal(tab)
                print("Приятного просмотра!")
            if x == "3":
                tab = P3[1]
                Pzal(tab)
                n = int(input("Сколько мест вы хотите забронировать: "))
                tab = Izal(tab, n)
                Pzal(tab)
                print("Приятного просмотра!")
        elif f == f3:
            Se(H3)
            x = input("Выберите время: ")
            for i in range(len(H3)):
                P1 = H3[i].T1
                P2 = H3[i].T2
                P3 = H3[i].T3
            if x == "1":
                tab = P1[1]
                Pzal(tab)
                n = int(input("Сколько мест вы хотите забронировать: "))
                tab = Izal(tab, n)
                Pzal(tab)
                print("Приятного просмотра!")
            if x == "2":
                tab = P2[1]
                Pzal(tab)
                n = int(input("Сколько мест вы хотите забронировать: "))
                tab = Izal(tab, n)
                Pzal(tab)
                print("Приятного просмотра!")
            if x == "3":
                tab = P3[1]
                Pzal(tab)
                n = int(input("Сколько мест вы хотите забронировать: "))
                tab = Izal(tab, n)
                Pzal(tab)
                print("Приятного просмотра!")

    elif n == 2:
        print("Вы можете отсортировать фильмы и информацию о них по:")
        print("1. Оценки MDB")
        print("2. Первой букве названия")
        print("3. Дате выпуска")
        k = int(input("ваш выбор: "))
        if k == 1:
            Sorted1()
        if k == 2:
            Sorted2()
        if k == 3:
            Sorted3()
    elif n == 3:
        SSS = ["США", "Новая_зеландия", "Франция", "Италия", "Япония", "СССР", "Великобритания"]
        print("В нашем кинотеатре представлены фильмы разных стран\nвы можете выбрать конкретную страну:")
        print("- США")
        print("- Новая_зеландия")
        print("- Франция")
        print("- Италия")
        print("- Япония")
        print("- СССР")
        print("- Великобритания")
        k = input("ваш выбор: ")
        if k in SSS:
            Con(A, k)
        else:
            print("Извините, но такой страны не представлено в списке.")

