class Queue:
    '''Реалізує чергу на базі списку.
    '''
    def __init__(self):
        '''Створити порожню чергу.
        '''
        self._lst = []                   #список елементів черги

    def isempty(self):
        '''Чи порожня черга?.
        '''
        return len(self._lst) == 0

    def add(self, data):
        '''Додати елемент в кінець черги.
        '''
        self._lst.append(data)           

    def take(self):
        '''Взяти елемент з початку черги.
        '''
        if self.isempty():
            print('Take: Черга порожня')
            exit(1)
        data = self._lst.pop(0)         #перший елемент черги - це нульовий елемент списку
        return data

    def __del__(self):
        '''Закінчити роботу з чергою.
        '''
        print('Deleting queue')
        del self._lst

a = Queue()                                 
n = int(input('Кількість1: '))
for i in range(n):
    pl = int(input('А(i+1)'))
    a.add(pl)

b = Queue()                                 
m = int(input('Кількість2: '))
for i in range(m):
    pl = int(input('B(i+1)'))
    b.add(pl)

c = Queue()
x = True
t2 = b.take()
while not (a.isempty() and b.isempty()):
    print(a._lst)
    print(b._lst)
    if x:
        t1 = a.take()
    else: t2 = b.take()
    if t1 < t2:
        x=True
        c.add(t1)
    else:
        x=False
        c.add(t2)
if x:
    c.add(t2)
print(c._lst)
