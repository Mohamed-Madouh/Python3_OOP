class student :
    def __init__(self):
        self.marks=[]
    def print_marks(self):
        print(self.marks)

    def add_mark(self,mark):
        self.marks.append(mark)


m = student()
m.add_mark(10)
m.add_mark(40)
m.add_mark(150)
m.add_mark(100)
m.add_mark(60)
m.add_mark(70)
m.print_marks()



n = student()
n.add_mark(30)
n.add_mark(60)
n.add_mark(15)
n.add_mark(18)
n.add_mark(90)
n.add_mark(7)
n.print_marks()


class a:
    def do(self):
        print('in a ')
class b(a):
    pass
class c :
    def do(self):
        print('in c ')
'''class d (c,b):
    pass'''
class d (b,c):
    pass
m=d()
m.do()
 
