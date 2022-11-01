class B:
    def __init__(self) -> None:
        self.b = 10
    def run(self):
        print(self.b)
class A:
    def __init__(self) -> None:
        self.b = B()
    def run(self):
        self.b.run()
    def getB(self):
        return self.b

def main():
    a = A()
    b = a.getB()
    b.b = 2
    a.run()

if __name__=='__main__':
    main()