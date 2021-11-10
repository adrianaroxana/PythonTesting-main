class Romania:
    def capitala(self):
        print("Capitala Romaniei este Bucuresti")

    def limba(self):
        print("Limba Romaniei este romana")


class Germania:
    def capitala(self):
        print("Capitala Germaniei este Berlin")

    def limba(self):
        print("Limba Germaniei este germana")


obj_ro = Romania()    #instantiem un obiect din Romania
obj_ger = Germania()    #instantiem un obiect din Germania

for element in (obj_ro, obj_ger):
    element.capitala()
    element.limba()


