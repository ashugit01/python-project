class Streetfood:
    def hygenic(self):
        print("no")
class panipuri(Streetfood):
    def taste(self):
        print("delicious")
class kaalan(Streetfood):
    def smell(self):
        print("wonderfull")
class bealpuri(Streetfood):
    def presentation(self):
        print("ok")
ob=bealpuri()
ob.hygenic()
ob.presentation()

ob=kaalan()
ob.hygenic()
ob.smell()

     