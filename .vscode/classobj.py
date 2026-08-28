class Laptop:
    window_version=11
    def performance(self):
        print("good")
    def storage(self):
        print("high")
hp=Laptop()
hp.window_version=12
print(hp.window_version)
hp.performance()
hp.storage()
dell=Laptop()
dell.performance()
dell.storage()
