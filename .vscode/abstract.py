class Supermarket:
    def fruits(self):
        pass
    def stationaryitem(self):
        pass
    def grosarry(self):
        pass
class rates(Supermarket):
    def fruits(self):
        print("rate is starts from 50")
    def stationaryitem(self):
        print("rate is starts from 5")
    def grosarry(self):
        print("rate is starts from 100")
ob=rates()
ob.fruits()
ob.stationaryitem()
ob.grosarry()                     