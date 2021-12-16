import math

print('''        Hej. 
        Jestem pomocnym programem z mechaniki płynów. Co chciałbyś policzyć?
            1 - Lepkość 
            2 - Parametry łożyska ślizgowego 
            3 - Napór hydrostatyczny działający na płaską klapę 
            4 - Obliczanie przepływu w rurze (spadek ciśnienia, objętościowe natężenie przepływu, średnica rury)
            5 - Obliczanie prędkości opadania kulki
            6 - Obliczanie niebezpiecznej prędkości dla komina
            7 - Przepływ w utwartym kanale
            ''')

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
                    f = 1  # f to f początkowe
                    df = 1
                    while df > 1e-6:
                        f1 = 1 / (1.14 - 2 * math.log10(e / D + 9.35 / (Re * math.sqrt(f)))) ** 2  # f1 to f końcowe
                        df = math.fabs(f - f1)  # fabs liczba zmiennoprzecinkowa dodatnia, f rzeczywisa
                        f = f1
                return f


            print('''**********************************************
                    Obliczania przepływu w rurze''')

            znak = 'T'

            while znak == 'T':
                # or znak == 't'
                # dane

                L = float(input('\nDługość rury [m] '))
                e = float(input('\nChropowatość [mm] '))
                e = e / 1000  # chropoatość Przeliczenie mm na metry
                rho = float(input('\nGęstośc płynu [kg/m^3] '))
                mu = float(input('\nLepkość płynu [Pa*s] '))

                print('''=== Wybierz parametr do obliczenia ===
                    1 - Spadek ciśnienia
                    2 - Objętościowe natężenie pzepływu
                    3 - Średnicę rury
                    4 - Wydatek przepływu i prędkość wypływu z rury o danym kącie nachylenia
                    ===========================================''')

                # Koniec wprowadzania danych

                wybor = int(input('\n Wybierz 1, 2 lub 3 '))

                if wybor == 1:
                    Q = float(input('\nObjętościowe natężenie przepływu [m3/s] '))
                    D = float(input('\nŚrednica rury [m] '))

                    v = 4 * Q / (math.pi * D ** 2)

                    Re = rho * v * D / mu

                    print('\nLiczba Reynoldsa wynosi Re = ', Re)

                    f = wsp(Re, e, D)

                    dp = f * L / D * rho * v ** 2 / 2
                    print('\n==================== Wynik =================')
                    print('\nSpadek ciśnienia wynosi ', dp, 'Pa')

                if wybor == 2:
                    dp = float(input('\nRóżnica ciśnień na końcach rur [Pa] '))
                    D = float(input('\nŚrednica rury [m] '))

                    v = dp * D ** 2 / (32 * mu * L)

                    Re = rho * v * D / mu

                    if Re < 2300:
                        Q = v * math.pi * D ** 2 / 4
                        print('\n Objętościowy wydatek przepływu wynisi ', Q, ' m^3/s')
                        print('\n Pędkośc przepływu wynisi ', v, ' m/s')
                        print('\n Przepływ laminarny')
                    else:
                        c = 2 * D * dp / (L * rho)
                        blad = 1.
                        while blad > 1e-6:
                            v1 = v
                            Re = rho * v * D / mu
                            f = wsp(Re, e, D)
                            v = math.sqrt(c / f)
                            blad = math.fabs(v - v1)
                        Q = v * math.pi * D ** 2 / 4
                        print('\n Objętościowy wydatek przepływu wynisi ', Q, ' m^3/s')
                        print('\n Pędkośc przepływu wynisi ', v, ' m/s')
                        print('\n Przepływ turbulentny')

                if wybor == 3:
                    dp = float(input('\nRóżnica ciśnień na końcach rur [Pa] '))
                    Q = float(input('\nNatężenie pzepływu [m^3/s] '))
                    D = (128 * mu * L * Q / (math.pi * dp)) ** 0.25
                    v = 4 * Q / (math.pi * D ** 2)
                    Re = rho * v * D / mu

                    if Re < 2300:
                        print('\nŚrednica wynosi ', D, ' m')
                        print('\n Przepływ laminarny')
                    else:
                        c = 8 * L * rho * Q ** 2 / (math.pi ** 2 * dp)

                        blad = 1.
                        while blad > 1e-6:
                            D1 = D
                            Re = rho * v * D / mu
                            f = wsp(Re, e, D)
                            D = (c * f) ** 0.2
                            blad = math.fabs(D - D1)

                        print('\nŚrednica wynosi ', D, ' m')
                        print('\n Przepływ turbulentny')

                if wybor == 4:
                    alfa = float(input('\nKąt nachylenia w stopniach '))
                    D = float(input('\nŚrednica rury [cm] '))
                    #v = math.sqrt(A/(1 + f * B))
                    Q = v*math.pi*D**2/4

                    if Re < 2300:
                        print('\nPrędkość przepływu wynosi ', v, ' m/s')
                        print('\n Wydatek przepływu wynosi ', Q, 'm^3/s')
                    else:


                        blad = 1.
                        while blad > 1e-6:
                            f = wsp(Re, e, D)
                            v1 = v
                            blad = math.fabs(D - D1)

                        Q = v * math.pi * D ** 2 / 4
                        print('\nPrędkość przepływu wynosi ', v, ' m/s')
                        print('\n Wydatek przepływu wynosi ', Q, 'm^3/s')

                znak = input('\nCzy chcesz powtórzyć obliczenia? (T/N) ')
                znak = znak.upper()

            break

        elif wybor == 5:
            print('''*******************************
                Obliczanie prędkości opadania kulki
                *************************************''')

            # Dane

            D = float(input('\nŚrednica [m] '))
            rhoK = float(input('\nGęstość kuli [kg/m^3] '))
            rhoP = float(input('\nGęstość płynu [kg/m^3] '))
            mu = float(input('\nLepkość [Pa*s] '))

            print('=' * 80)

            v = 9.81 * D ** 2 * (rhoK - rhoP) / (18 * mu)  # prędkość
            Re = rhoP * v * D / mu

            if Re < 10:
                print('\nPrędkość kuli v = ', v, ' m/s')
                print('\nRe = ', Re)
            else:
                alpha = 4 * D * 9.81 * (rhoK - rhoP) / (3 * rhoP)
                err = 1
                i = 1
                while err > 1e-6:
                    Re = rhoP * v * D / mu
                    CD = 24 / Re + 6 / (1 + math.sqrt(Re)) + 0.4
                    v1 = v
                    v = math.sqrt(alpha / CD)
                    err = math.fabs(v - v1)
                    i = i + 1
                    if i > 1000:
                        print('przekroczono 1000 iteracji')
                        exit()
                print('\Prędkość opadania kulki v = ', v, ' m/s')

        elif wybor == 6:
            print('''*******************************
                Obliczanie niebezpiecznej prędkości dla komina
                *************************************''')

            # Dane

            D = float(input('\nŚrednica komina [m] '))
            d = float(input('\nŚrednica wewnętrzna komina [m] '))
            H = float(input('\nWysokość komina [m] '))
            rhoP = float(input('\nGęstość płynu [kg/m^3] '))
            mu = float(input('\nLepkość [Pa*s] '))
            sigmadop = float(input('\nDopuszczalne naprężenie [MPa] '))
            sigmadop = sigmadop * 1000  # na pascale

            print('=' * 80)

            W = math.pi * (D ** 4 - d ** 4) / (32 * D)
            # Mg = sigmadop*W
            Mg = 1151.19
            alpha = 4 * Mg / (rhoP * H ** 2 * D)
            err = 1
            v = 1
            i = 1

            while err > 1e-6:
                Re = rhoP * v * D / mu
                CD = 1 + 10 / Re ** 0.67
                v1 = v
                v = math.sqrt(alpha / CD)
                err = math.fabs(v - v1)
                i = i + 1
                if i > 1000:
                    print('przekroczono 1000 iteracji')
                    exit()
            print('\Prędkość opadania kulki v = ', v * 3.6, ' km/h')

        elif wybor == 7:
            def prostokat():
                Y = 1.  # zmienna rzczywista
                err = 1.
                while err > 1e-6:
                    A = 2 * Y + B  # zmienna pomocnicza, żeby zbyt wiele nie pisać
                    F = Y ** (5. / 3.) / A ** (2. / 3.) - n * Q / (B ** (5. / 3.) * math.sqrt(s))
                    DF = (5. / 3.) * Y ** (2. / 3.) * A ** (2. / 3.) - (4. / 3.) * Y ** (5. / 3.) * A ** (
                                -1. / 3.) / A ** (4. / 3.)  # pochodna F
                    Y1 = Y  # nowy igrek
                    Y = Y - F / DF
                    err = math.fabs(Y - Y1)
                return Y


            def trapez():
                Y = 1.  # zmienna rzczywista
                err = 1.
                while err > 1e-6:
                    A = math.sqrt(1 + Z ** 2)  # zmienna pomocnicza, żeby zbyt wiele nie pisać
                    F = ((B + Y * Z) * Y) ** (5. / 3.) / (B + 2 * Y * A) ** (2. / 3.) - n * Q / math.sqrt(s)
                    DF = ((B + Y * Z) * Y) ** (2. / 3.) * (
                                10 * Y * Z * B + 16 * Y ** 2 * Z * A + 5 * B ** 2 + 6 * B * Y * A) / (
                                 B + 2 * Y * A) ** (5. / 3.)  # pochodna F
                    Y1 = Y  # nowy igrek
                    Y = Y - F / DF
                    err = math.fabs(Y - Y1)
                return Y


            import math

            print('''
            OBLICZANIE GŁĘBOKOŚCI KANAŁU
            ''')

            Q = float(input('\nObjęościowe naężenie przepłyu [m^3/s] '))
            n = float(input('\nWspółczynnik Manninga [s/m^1/3] '))
            s = float(input('\nPochylenie podłużne '))

            print("""\n Wybierz kształt kanału
                1 - prostokątny
                2 - trójkąny
                3 - trapezowy
                4 - cylindryczny""")

            wybor = int(input('\nKróty kanałwybierasz? '))

            if wybor == 1:
                B = float(input('\nSzerokość dna [m] '))
                Y = prostokat()

            elif wybor == 2:
                gama = float(input('\nKąt odchylenia ścian bocznych od pionu [stopnie] '))
                Z = math.tan(gama * math.pi / 180)
                Y = (n * Q) ** (3. / 8.) / Z ** (5. / 8.) * (2 * math.sqrt(Z ** 2 + 1) ** 0.25 / s ** (3. / 16.))


            elif wybor == 3:
                B = float(input('\nSzerokość dna [m] '))
                beta = float(input('\nKąt odchylenia ścian bocznych od pionu [stopnie] '))
                Z = math.tan(beta * math.pi / 180)
                Y = trapez()

            print("\nGłębokość kanału ", Y, "m")

    start = input('Czy chcesz wyjśc z programu? '
                  'Wpisz NIE jeżeli nie chcesz wyjść lub cokolwiek jeżeli chcesz wyjsć \n')
    start = start.upper()
    continue


