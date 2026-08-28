class Arundhathi:
    def movietype(self):
        print("very horror")
class arundhathi(Arundhathi):
    def heroine(self):
        print("anushka shetty act as heroine")
class anwar(Arundhathi):
    def helpingcharacter(self):
        print("this is sayaji shinde's role")
class pasupathi(Arundhathi):
    def villain(self):
        print("sonu sood act as a terrifying and evil black magician")
class devimovie(pasupathi):
    def lovingcharacter(self):
        print("in this movie sonu sood fall in love with thammana")

ob=anwar()
ob.helpingcharacter()
ob.movietype()

ob=devimovie()
ob.lovingcharacter()
ob.villain()
ob.movietype()
                                              

