import numpy as np

class A:
    def __init__(self) -> None:
        self.a = 10
        self.b = 50
        self.c = 60
    def run(self):
        print(self.c)
class B(A):
    def __init__(self) -> None:
        super().__init__()
    def run(self):
        print(self.a)

def main():
    a = [1,1,1]
    b = a.index(max(a))
    print(b)

if __name__=='__main__':
    main()