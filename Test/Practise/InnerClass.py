class Employee:

    class Laptop:

        def show(self):
            print("from the inner class")


class B(Employee.Laptop):
    def metB(self):
        print("From method B")



b=B()
b.show()
