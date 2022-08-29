import logging
logging.basicConfig(level=logging.DEBUG)

dzialanie=input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
if dzialanie=="1":
    liczba_skladnikow=input("Podaj liczbę składników: ")
    skladniki=[]
    wynik=0
    for i in range(0, int(liczba_skladnikow)):
        skladnik=input("Podaj kolejny składnik. ")
        skladniki.append(skladnik)
        wynik=wynik+float(skladnik)
    logging.info("Dodaję %.0f składniki(ów)" %(len(skladniki)))

elif dzialanie=="2":
    liczba1=input("Podaj odjemną. ")
    liczba2=input("Podaj odjemnik. ")
    logging.info("Od %.2f odejmuję %.2f." %(float(liczba1), float(liczba2)))
    wynik = float(liczba1) - float(liczba2)

elif dzialanie=="3":
    liczba1=input("Podaj czynnik 1. ")
    liczba2=input("Podaj czynnik 2. ")
    logging.info("Mnożę %.2f i %.2f." %(float(liczba1), float(liczba2)))
    wynik = float(liczba1) * float(liczba2)

elif dzialanie=="4":
    liczba1=input("Podaj dzielną. ")
    liczba2=input("Podaj dzielnik. ")
    if liczba2=="0":
        wynik="Kto dzieli przez 0, ten się w piekle poniewiera."
    elif liczba2!=0:
        logging.info("Dzielę %.2f przez %.2f." %(float(liczba1), float(liczba2)))
        wynik = float(liczba1) / float(liczba2)

if dzialanie=="4" and liczba2=="0":
    print(wynik)
elif dzialanie!="1" and dzialanie!="2" and dzialanie!="3" and dzialanie!="4":
    print("Przykro mi - nie wykonałeś polecenia wg instrukcji.")
else:
    print("Wynik to %.2f" %(wynik))