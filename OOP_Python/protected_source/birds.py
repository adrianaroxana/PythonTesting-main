class Bird:
    def universal(self):
        print("It is a bird")
    def flight(self):
        print("Some birds fly, some others do not.")

class Sparrow(Bird):
    def flight(self):
        print("Sparrows fly.")

class Ostrich(Bird):
    def flight(self):
        print("Ostriches do not fly.")


b = Bird()
s = Sparrow()
o = Ostrich()

b.flight()
s.flight()
s.universal()
o.flight()
o.universal()