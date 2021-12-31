class Emp:

    def show(self):
        print("from Emp class")


class Lap:
    def show(self):
        print("from Lap class")

class Duck:

    def __init__(self,emp):
        self.name="Sagar"
        self.emp=emp

    def info(self):
        self.emp.show()

d=Duck(Emp())
d1=Duck(Lap())

d.info()
d1.info()