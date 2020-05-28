'''
# 1. Napisz program który obliczy pole kwadratu bazując na zmiennych jakie podał użytkownik.

a = int(input("podaj długość boku kwadratu: "))
print("pole kwadratu to: ", a*2)

#2. Napisz program który obliczy obwód kwadratu bazując na zmiennych jakie podał użytkownik.

a = int(input("podaj długość boku kwadratu: "))
print("obwód kwadratu to: ", a*4)


#3. Napisz program który obliczy pole prostokąta bazując na zmiennych jakie podał użytkownik.
a = int(input("podaj długość 1 boku prostokąta: "))
b = int(input("podaj długość 2 boku prostokąta: "))
print("pole prostokąta to: ", a*b)


#4. Napisz program który obliczy obwód prostokąta bazując na zmiennych jakie podał użytkownik.

a = int(input("podaj długość pierwszego boku prostokąta: "))
b = int(input("podaj długość drugiego boku prostokąta: "))
print("obwód prostokąta to: ", 2*a+2*b)


#5. Napisz program który obliczy pole koła bazując na zmiennych jakie podał użytkownik (możesz założyć, że pi to 3.14).
# Zadanie 5
r = float(input("podaj promień koła: "))
print("pole koła to: ", 3.14*r**2)

#6. Napisz program który obliczy obwód koła bazując na zmiennych jakie podał użytkownik (możesz założyć, że pi to 3.14).
# Zadanie 6
r = float(input("podaj promień koła: "))
print("bbwód koła to: ", 2*3.14*r)

10. Napisz program który prosi użytkownika o podanie imienia i wieku. Następnie wypisuje ile lat brakuje użytkownikowi do 100 lat.

a = input("podaj imię: ")
b = int(input("podaj wiek: "))
print("do stu lat zostało ci" , 100-b )

11. Napisz program, który prosi użytkownika o podanie dowolnej liczby a następnie wypisał ją tyle razy ile była podana. np. gdy poda '5' powinno wypisać '5 5 5 5 5'

a = int(input("podaj liczbe: "))
b = str(a)
print(a*b)


#12. Napisz program który prosi użytkownika o podanie wartości. W zależności czy wartość jest parzysta lub niepatrzysta wypisz odpowieni komunikat

a = input ("podaj liczbę: ")
a = int(a)
b = a % 2

print(b)
if b == 0:
     print("liczba parzysta")
else b == 1:
     print("liczba nieparzysta")

'''

