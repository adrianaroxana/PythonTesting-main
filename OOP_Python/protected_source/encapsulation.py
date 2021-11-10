from abc import ABC, abstractmethod


class BaseTestModel(ABC):
    @abstractmethod
    def test_def(self):
        raise NotImplemented

    @abstractmethod
    def test_exe(self):
        raise NotImplemented


class BaseTest(BaseTestModel):
    def __init__(self, name, nr_steps):
        self._name = name
        self._nr_steps = nr_steps

    def test_def(self):
        print("I am currently starting the test case")

    def test_exe(self):  # when we overwrite a method from a parent class = override
        print(f"I now execute {self._nr_steps} steps of the test case {self._name}")

    def test_rep(self):
        print("Generate a report")

    def tear_down(self):
        print("Quit driver connectivity")

    def internal_logger(self):  # functionalitate prin care afisam loguri
        print("public method") # public method cand be called from everywhere

    def _internal_logger(self):
        print("protected method")  # we need the _ for protected method - can be called within the class and within the package

    def __internal_logger(self):
        print("private method")  # private methods defined with__  - can be called only within the class where it is defined
    def internal_logger_private(self):
        self.__internal_logger()

test_case = BaseTest("TestCase1", 3)
test_case.test_rep()
test_case.test_exe()
test_case.test_def()
test_case.internal_logger()
test_case._internal_logger()
test_case.internal_logger()