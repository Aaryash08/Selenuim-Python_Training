from abc import ABC,abstractmethod
class BANK(ABC):
    @abstractmethod
    def intrest(self):
        pass
    @abstractmethod
    def loan(self):
        pass

class SBI(BANK):
    def intrest(self):
        print("Interst is 6%")
    def loan(self):
        print("Loan is available")

s=SBI()
s.intrest()
s.loan()