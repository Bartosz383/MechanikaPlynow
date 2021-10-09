import math

print('''        Hej. 
        Jestem pomocny programem z mechaniki płynów. Co chciałbyś policzyć?
            1 - Lepkość 
            2 - Parametry łożyska ślizgowego 
            3 - Napór hydrostatyczny działający na płaską klapę ''')

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
            print('''      
                            1 - Kształt połowy koła
                            2 - Kształt koła z kołowym wycięciem
                            3 - Kształt prostokąta z doklejonym trapezem
                            4 - Kształt zaokrąglonego prostokąta''')

            WewnetrznyWybor = int(input('\n Wybierz kształt klapy '))
            break
        elif wybor == 4:
            print('''      
                            1 - Kształt połowy koła
                            2 - Kształt koła z kołowym wycięciem
                            3 - Kształt prostokąta z doklejonym trapezem
                            4 - Kształt zaokrąglonego prostokąta''')

            WewnetrznyWybor = int(input('\n Wybierz kształt klapy '))
            break
        else: print('\n Wybór nieprawidłowy')

    start = input('Czy chcesz wyjśc z programu? '
                  'Wpisz NIE wielkimi literami jeżeli nie chcesz wyjść lub cokolwiek jeżeli chcesz wyjsć \n')
    continue


