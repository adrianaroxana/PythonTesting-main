from abc import ABC, abstractmethod


#decorator este o modalitate de a altera comportamentul unei functii



class TestModel(ABC):  #ABC = abstract base class
    @abstractmethod
    def setup(self):
        pass #facem o functie pe care nu stim exact inca cum o s -o implementam


    @abstractmethod
    def execute(self):
        raise NotImplemented  #anuntam utilizatorul viitor/sistemul ca block-code-ul pt aceasta metoda a fost implementat


    @abstractmethod
    def tear_down(self):
        raise NotImplemented


class TC1(TestModel):
    def setup(self):
        print("am setat parametrii test case-ului")

    def execute(self):
        print("acum executam test case-ul")

    def tear_down(self):
        print("inchidem test case-ul dupa executie")




testCase = TC1()
testCase.setup()
testCase.execute()
testCase.tear_down()


#functiile unei clase se pot apela doar cu ajutorul obiectului
obiect.metodaClasa()