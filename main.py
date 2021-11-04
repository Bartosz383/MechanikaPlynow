import math

print('''        Hej. 
        Jestem pomocny programem z mechaniki płynów. Co chciałbyś policzyć?
            1 - Lepkość 
            2 - Parametry łożyska ślizgowego 
            3 - Napór hydrostatyczny działający na płaską klapę 
            4 - Obliczanie spadku cisnienia w rurze ''')

start = 'NIE'
while start == 'NIE':
    while True:
        wybor = int(input('\n Wprowadź nr operacji '))
        if wybor == 1:
            print('''      
                        1 - Lepkość lepkościomierzem kapilarnym
                        2 - Lepkość lepkościomierzem z kulką
                        3 - Lepkość lepkościomierzem rotacyjnym''')

            WewnetrznyWybor = int(input('\n Wybierz operacje '))

            if WewnetrznyWybor == 1:
                print('\n Wybrałeś lepkościomierz kapilarny ')
                print('Wprowadź dane: ')
                L = float(input('\n Długość kapilary [m] '))
                d = float(input('\n Średnica kapilary [mm] '))
                d /= 1000                                                           # zamiana mm na metry
                dp = float(input('\n Różnica ciśnie [Pa] '))
                Q = float(input('\n Objętościowe natężenie przepływu [m^3/s] '))
                mi = math.pi*dp*d**4/(128*L*Q)
            elif WewnetrznyWybor == 2:
                print('\n Wybrałeś lepkościomierz z kulką ')
                print('Wprowadź dane: ')
                L = float(input('\n Długość odcina jaki przebyła kulka [m] '))
                d = float(input('\n Średnica kulki [mm] '))
                d /= 1000  # zamiana mm na metry
                t = float(input('\n Czas spadania kulki [s] '))
                roK = float(input('\n Gęstość kulki [kg/m^3] '))
                roP = float(input('\n Gęstość płynu [kg/m^3] '))
                mi = d ** 2 * (roK * 9.81 - roP * 9.81) * t / (18 * L)
            elif WewnetrznyWybor == 3:
                print('\n Wybrałeś lepkościomierz rotacyjny ')
                print('Wprowadź dane: ')
                L = float(input('\n Długość cylindra [m] '))
                omega = float(input('\n Prędkość kątowa wirującego cylindra [1/s] '))
                M = float(input('\n Moment obrotowy działający na ruchomy cylinder [Nm] '))
                h = float(input('\n Szerokość szczeliny między cylindrami [m] '))
                h /= 1000000
                R = float(input('\n Promień wirującego cylindra [mm]'))
                R /= 1000
                mi = M * h / (2 * math.pi * R ** 3 * L * omega)
            else: print('\n Wybór nieprawdłowy')
            print('\n******************** WYNIK ******************')
            print('\n Lepkość płynu wynosi ', mi, 'Pa*s')
            break

        elif wybor == 2:
            print('\n Wybrałeś siłę nośną łożyska, moment tarcia lepkiego i moc rozpraszana na łożysku ')
            print('Wprowadź dane: ')
            L = float(input('\n Długość wirującego czopa [mm] '))
            L /= 1000
            D = float(input('\n Średnica wirującego czopa [mm] '))
            D /= 1000
            R = D/2
            n = float(input('\n Prędkośc obrotowa wirującego cylindra [obr/min] '))
            n /= 60
            omega = 2*math.pi*n
            h = float(input('\n Średni luz promieniowy pomiędzy czopem i panewką [mm] '))
            h /= 1000
            mi = float(input('\n Lepkość oleju [Pa*s] '))
            epsilon = float(input('\n Mimośród wzgędny '))
            F = 12 * math.pi * mi * R ** 3 * L * omega * epsilon / \
                (h ** 2 * (2 + epsilon ** 2) * (1 - epsilon ** 2) ** (1 / 2))
            M = 2 * math.pi * mi * R ** 3 * L * omega / h
            P = 2 * math.pi * mi * R ** 3 * L * omega**2 / h

            print('\n******************** WYNIKI ******************')
            print('\n Siłę nośną łożyska ', F, 'N')
            print('\n Moment tarcia lepkiego ', M, 'Nm')
            print('\n Moc rozpraszaną na łożysku wskutek lepkosci oleju ', P, 'W')
            break

        elif wybor == 3:
            AG = 0.0;
            SXG = 0.0;
            SYG = 0.0;
            IYG = 0.0;
            IXYG = 0.0
            rho = float(input("\n Podaj gestosc cieczy [kg/m^3]: "))
            alpha = float(input("Podaj kąt nachylenia ściany (w stopniach): "))
            print('''
            -----------------------------------------------"
             UWAGA! dla kazdego obszaru podajemy 'kod'
             Jesli element stanowi wyciecie wprowadz kod = -1
                         w przeciwnym razie wprowadz kod = 1

             ------ OBSZARY W KSZTALCIE KOLA ----------''')
            nkol = int(input("\nLiczba obszarow w ksztalcie kola: "))
            for i in range(nkol):
                kod = int(input("Wprowadz kod %d-go kola " % (i + 1)))
                xk = float(input("x wspolrzedna środka %d-go kola " % (i + 1)))
                yk = float(input("y wspolrzedna śodka %d-go kola " % (i + 1)))
                r = float(input("promien %d kola " % (i + 1)))
                A = math.pi * r ** 2 * kod                                      # pole powierzchni
                SX = yk * A;                                                    #
                SY = xk * A                                                     #
                AG = AG + A;                                                    #
                SXG = SXG + SX;                                                 #
                SYG = SYG + SY                                                  #
                IYG = IYG + A * r ** 2 / 4.0 + A * xk ** 2                      #
                IXYG = IXYG + A * xk * yk                                       #
            print("\n------ OBSZARY W KSZTALCIE POLKOLA ----------")
            nkol = int(input("\nLiczba obszarow w ksztalcie polkola: "))
            for i in range(nkol):
                kod = int(input("\nWprowadz kod %d-go polkola " % (i + 1)))
                xk = float(input("x wspolrzedna srodka cieciwy %d-go polkola " % (i + 1)))
                yk = float(input("y wspolrzedna srodka cieciwy %d-go polkola " % (i + 1)))
                r = float(input("promien %d półkola " % (i + 1)))
                beta = float(input(
                    "KAT MIERZONY PRZECIWNIE DO RUCHU WSKAZOWEK ZEGARA MIEDZY OSIA OX A OSIA SYMETRII POLKOLA SKIEROWANa W STRONe WYPUKLOSCI (w stopniach)"))
                beta = beta * math.pi / 180.0
                A = math.pi * r ** 2 * kod / 2.0
                c = 4.0 * r / math.pi / 3.0
                xc = xk + c * math.cos(beta)
                yc = yk + c * math.sin(beta)
                SX = yc * A;
                SY = xc * A
                AG = AG + A;
                SXG = SXG + SX;
                SYG = SYG + SY
                IYG = IYG + (A * r * r / 4.0 - A * c ** 2 * math.cos(beta) ** 2) + A * xc ** 2
                IXYG = IXYG + c * c * A / 2 * math.sin(-2 * beta) + A * xc * yc
            print("\n------ OBSZARY W KSZTALCIE WIELOKATA ----------")
            print("\nWspolrzedne wierzcholkow nalezy wprowadzac po kolei zgodnie z kierunkiemruchu wskazowek zegara")
            nwiel = int(input("\nLiczba obszarow w ksztalcie wielokąta: "))
            for j in range(nwiel):
                X = [];
                Y = []
                print('WPROWADZ kod', j + 1, ' WIELOKATA')
                kod = int(input("kod = "))
                n = int(input("Liczba wierzcholkow %d-go wielokata wynosi " % (j + 1)))
                for i in range(n):
                    print("Podaj wspolrzedne", i + 1, "wierzcholka")
                    X.append(float(input("Wspolrzedna x ")))
                    Y.append(float(input("Wspolrzedna y ")))
                X.append(X[0])
                Y.append(Y[0])
                #	print x
                A = 0.0;
                SX = 0.0;
                SY = 0.0;
                IY = 0.0;
                IXY = 0.0
                for I in range(n):
                    A = A + (X[I + 1] - X[I]) * (Y[I + 1] + Y[I])
                    SX = SX + (X[I + 1] - X[I]) * (Y[I] * Y[I] + Y[I] * Y[I + 1] + Y[I + 1] * Y[I + 1])
                    SY = SY + (Y[I] - Y[I + 1]) * (X[I] * X[I] + X[I] * X[I + 1] + X[I + 1] * X[I + 1])
                    IY = IY + (Y[I] - Y[I + 1]) * (
                                X[I] ** 3 + X[I] * X[I] * X[I + 1] + X[I] * X[I + 1] * X[I + 1] + X[I + 1] ** 3)
                    IXY = IXY + (X[I + 1] - X[I]) * (
                                X[I] * (3.0 * Y[I] ** 2 + Y[I + 1] ** 2 + 2.0 * Y[I] * Y[I + 1]) + X[I + 1] * (
                                    3.0 * Y[I + 1] ** 2 + Y[I] ** 2 + 2.0 * Y[I] * Y[I + 1]))
                A = kod * A / 2.0;
                SX = kod * SX / 6.0;
                SY = kod * SY / 6.0
                IY = kod * IY / 12.0;
                IXY = kod * IXY / 24.0
                SXG = SXG + SX
                SYG = SYG + SY
                AG = AG + A
                IYG = IYG + IY
                IXYG = IXYG + IXY
            XC = SYG / AG;
            YC = SXG / AG
            print("\n\n======== WYNIKI ===========")
            print("\nPole obszaru wynosi", AG)
            print("SXG= ", SXG, "SX= ", SX)
            print("\nWspolrzedne srodka ciezkosci ")
            print("XC = ", XC)
            print("YC = ", YC)
            print("\nWspolrzedne srodka parcia")
            print("XS =", IYG / SYG)
            print("YS =", IXYG / SYG)
            print("\nSila parcia")
            print("F = ", 9.81 * rho * AG * XC * math.sin(alpha * math.pi / 180))
            break

        elif wybor == 4:

            def wsp(Re, e, D):
                if Re < 2300:
                    f = 64 / Re
                elif Re < 4000:
                    f = 2.82 * e - 7 * Re ** 1.5
                else:
                    f = 1                                                                           # f to f początkowe
                    df = 1
                    while df > 1e-6:
                        f1 = 1 / (1.14 - 2 * math.log10(e / D + 9.35 / (Re * math.sqrt(f)))) ** 2  # f1 to f końcowe
                        df = math.fabs(f - f1)                   # fabs liczba zmiennoprzecinkowa dodatnia f rzeczywisa
                        f = f1
                return f

             # dane

            L = float(input('\nDługość rury [m] '))
            D = float(input('\nŚrednica rury [m] '))
            e = float(input('\nChropowatość [mm] '))
            e = e / 1000  # Przeliczenie mm na metry
            rho = float(input('\nGęstośc płynu [kg/m^3] '))
            mu = float(input('\nLepkość płynu [Pa*s] '))
            Q = float(input('\nObjętościowe natężenie przepływu [m3/s] '))

            # Koniec wprowadzania danych

            v = 4 * Q / (math.pi * D ** 2)

            Re = rho * v * D / mu

            print('\nLiczba Reynoldsa wynosi Re = ', Re)

            f = wsp(Re, e, D)

            dp = f * L / D * rho * v ** 2 / 2
            print('\n==================== Wynik =================')
            print('\nSpadek ciśnienia wynosi ', dp, 'Pa')
            break


    start = input('Czy chcesz wyjśc z programu? '
                  'Wpisz NIE jeżeli nie chcesz wyjść lub cokolwiek jeżeli chcesz wyjsć \n')
    start = start.upper()
    continue


