class Car:  # numele claselor incepe cu litera mare si urmeaza camel case, variabilele si functiile se vor scrie mereu cu litera mica
    # si vor urma snake case
    def start_car(self):
        print("Masina trebuie sa porneasca atunci cand porneste motorul")

    def stop_car(self):
        print("Masina trebuie sa se opreasca atunci cand se opreste motorul")

    # functii in clasa = metode


class OldCar(Car):  # mostenirea se face pe baza plasarii intre paranteze a numelui clasei parinte
    def start(self):
        print("Masina trebuie sa porneasca atunci cand cheia este spre dreapta")

    def stop(self):
        print("Masina trebuie sa se opreasca atunci cand cheia spre stanga")


class NewCar(Car):
    def start(self):
        print("Masina trebuie sa porneasca atunci cand apesi butonul start")

    def stop(self):
        print("Masina trebuie sa se opreasca atunci cand apesi butonul stop")


masina1 = Car()  # se apeleaza metoda start din clasa Car
masina2 = OldCar()
masina3 = NewCar()

masina1.start_car()
masina2.start()
masina2.start_car()
masina3.start()
