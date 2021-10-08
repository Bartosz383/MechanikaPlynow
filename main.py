import math

print('''        Hej. 
        Jestem progamem do wyznaczania lekości przy pomocy lepkościomierza. 
        Chcesz coś policzyć?
            1 - lepkościomierz kapilarny
            2 - lepkościomierz z kulką
            3 - lepkościomierz rotacyjny''')


wybor = int(input('\n Wprowadź nr lepkościomierza '))

if wybor == 1:
    print('\n Wybrałeś lepkościomierz kapilarny ')
    print('Wprowadź dane: ')
    L = float(input('\n Długość kapilary [m] '))
    d = float(input('\n Średnica kapilary [mm] '))
    d /= 1000                                                           # zamiana mm na metry
    dp = float(input('\n Różnica ciśnie [Pa] '))
    Q = float(input('\n Objętościowe natężenie przepływu [m^3/s] '))
    mi = math.pi*dp*d**4/(128*L*Q)
elif wybor == 2:
    print('\n Wybrałeś lepkościomierz z kulką ')
    print('Wprowadź dane: ')
    L = float(input('\n Długość odcina jaki przebyła kulka [m] '))
    d = float(input('\n Średnica kulki [mm] '))
    d /= 1000                                                           # zamiana mm na metry
    t = float(input('\n Czas spadania kulki [s] '))
    roK = float(input('\n Gęstość kulki [kg/m^3] '))
    roP = float(input('\n Gęstość płynu [kg/m^3] '))
    mi = d**2*(roK*9.81-roP*9.81)*t/(18*L)
elif wybor == 3:
    print('\n Wybrałeś lepkościomierz rotacyjny ')
    print('Wprowadź dane: ')
    L = float(input('\n Długość cylindra [m] '))
    omega = float(input('\n Prędkość kątowa wirującego cylindra [1/s] '))
    M = float(input('\n Moment obrotowy działający na ruchomy cylinder [Nm] '))
    h = float(input('\n Szerokość szczeliny między cylindrami [m] '))
    h /= 1000000
    R = float(input('\n Promień wirującego cylindra [mm]'))
    R /= 1000
    mi = M*h/(2*math.pi*R**3*L*omega)
else: print('\n Wybór nieprawidłowy')
print('\n******************** WYNIK ******************')
print('\n Lepkość płynu wynosi ', mi, 'Pa*s')
