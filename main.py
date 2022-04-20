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