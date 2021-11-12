class Dog():
    def __init__(self,nom):
        self.nom=nom
    def return_nom(self):
        print(self.nom)

    def square(self,number):
        return number ** 2

class animal():
    def __init__(self,nom):
        self.nom=nom
    def return_nom(self):
        print(self.nom)

    def square(self,number):
        return number ** 2

def square(number):
    return number**2

chien = Dog("lassi")

chien.return_nom()

test = lambda x : chien.square(x)
print(test)
print(test(9))
print(chien.square(10))

(chien
 | "test_chargement" >> animal("mammifere"))

