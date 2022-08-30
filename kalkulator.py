import logging

logging.basicConfig(level=logging.DEBUG)


def dodawanie(liczba1, liczba2):
    return liczba1 + liczba2


def odejmowanie(liczba1, liczba2):
    return liczba1 - liczba2


def mnozenie(liczba1, liczba2):
    return liczba1 * liczba2


def dzielenie(liczba1, liczba2):
    if liczba2 == 0:
        return "Kto dzieli przez 0, ten się w piekle poniewiera"
    else:
        return liczba1 / liczba2


if __name__ == "__main__":
    dzialanie = input(
        "Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "
    )
    if dzialanie not in ["1", "2", "3", "4"]:
        print("Przykro mi, nie wykonałeś polecenia poprawnie.")
    else:

        if dzialanie == "1":
            liczba_skladnikow = input("Podaj liczbę składników: ")
            skladniki = []
            wynik = 0
            for i in range(int(liczba_skladnikow)):
                skladnik = float(input("Podaj kolejny składnik. "))
                skladniki.append(skladnik)
                if i == 0:
                    pass
                else:
                    logging.info("Dodaję %.2f i %.2f" % (wynik, skladnik))
                wynik = dodawanie(wynik, skladniki[i])

        elif dzialanie == "2":
            liczba1 = float(input("Podaj odjemną. "))
            liczba2 = float(input("Podaj odjemnik. "))
            logging.info("Od %.2f odejmuję %.2f." % (liczba1, liczba2))
            wynik = odejmowanie(liczba1, liczba2)

        elif dzialanie == "3":
            liczba_czynnikow = float(input("Podaj liczbę czynników: "))
            czynniki = []
            wynik = 1
            for i in range(int(liczba_czynnikow)):
                czynnik = float(input("Podaj kolejny czynnik. "))
                czynniki.append(czynnik)
                if i == 0:
                    pass
                else:
                    logging.info("Mnożę %.2f i %.2f." % (wynik, czynnik))
                wynik = mnozenie(wynik, czynniki[i])

        elif dzialanie == "4":
            liczba1 = float(input("Podaj dzielną. "))
            liczba2 = float(input("Podaj dzielnik. "))
            logging.info("Dzielę %.2f przez %.2f." % (liczba1, liczba2))
            wynik = dzielenie(liczba1, liczba2)

        if dzialanie == "4" and liczba2 == 0:
            print(wynik)
        else:
            print("Wynik to: %.2f" % (wynik))
