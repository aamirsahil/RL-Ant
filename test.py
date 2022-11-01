class A:
    def __init__(self) -> None:
        self.a = 10
        self.b = 20
        self.c = {'x' : 30}
        self.B = B(self.c)
    def run(self):
        print(self.c)
        self.B.run()
class B():
    def __init__(self, c) -> None:
        self.c = c
    def run(self):
        self.c['x'] = 50

def main():
    a = A()
    a.run()
    a.run()

if __name__=='__main__':
    main()