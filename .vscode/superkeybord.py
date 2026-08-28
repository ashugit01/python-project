class a:
    def __init__(self):
        print("hii")
class b(a):
    def __init__(self):
        print("hello")
        super().__init__()
ob=b()
    