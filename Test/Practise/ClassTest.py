class Employee:

    company="NCR"
    def __init__(self,name,id):
        self.name=name
        self.id=id




    def show(self):
        print('{},{}'.format(self.name, self.id))

    @staticmethod
    def info():
        print("this is static method")

    @classmethod
    def classMet(cls):

        print(cls.company)



emp=Employee("Sagar",23)

emp.show()
emp.info()
Employee.classMet()
