class Dad:
    def nose(self):
        print("my dad have big nose from his gen")
class Mom:
    def faceshape(self):
        print("my mom had oval+round faceshape from her gen")
class Me(Dad,Mom):
    def both(self):
        print("i had big nose and oval+round faceshape from my parents")
ob=Me()
ob.nose()
ob.faceshape()
ob.both()        

