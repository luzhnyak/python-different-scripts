class _Selem:
    '''Реалізує кільцевий список на базі звізування об'єктів.
    '''
    def __init__(self,data):
        '''Створити порожній список.
        '''
        self._data = data               #список елементів
        self._next = None

class Rlist:
    def __init__(self):
        self._cur = None

    def isempty(self):
        '''Чи порожній список?.
        '''
        return self._cur == None

    def len(self):
        '''Довжина 
        '''        
        k=0
        if not self.isempty():
            elem = self._cur
            while elem._next!=self._cur:
                k+=1
                elem = elem._next
            return k+1
        else:
            return k

    def next(self):
        '''Перейти до наступного елемента.
        '''        
        if not self.isempty():
            self._cur = self._cur._next          

    def getcurrent(self):
        '''Повернути поточний елемент.
        '''        
        if not self.isempty():
            return self._cur._data           
        else:
            return None

    def update(self, data):
        '''Оновити поточний елемент.
        '''        
        if not self.isempty():
            self._cur._data = data

    def insert(self, data):
        '''Вставити елемент перед поточним.
        '''
        elem = _Selem(data)

        if not self.isempty(): #якщо список не порожній
            elem._data = self._cur._data
            elem._next = self._cur._next
            self._cur._data = data
            self._cur._next = elem
            self._cur = elem            
        else:
            self._cur = elem      #додаємо елемент, він стає поточним
            self._cur._next = elem

    def print(self):
        '''Друк
        '''
        sp=""
        if self.isempty():
           print("Список пустий")
        else:
            elem = self._cur
            while elem._next!=self._cur:
                sp=sp+elem._data+" "
                elem = elem._next
            sp = sp+elem._data
            print(sp)
        
    def delete(self):
        '''Видалити поточний елемент.
        '''
        if not self.isempty():
            if self._cur._next == self._cur:
                del self._cur  #якщо список після видалення елемента спорожнів
                self._cur = None
            else:
                elem = self._cur._next
                self._cur._data = elem._data
                self._cur._next = elem._next
                del elem                  

    def search (self, x):
        b = False
        if self.isempty():
           print("Список пустий")
        else:
            elem = self._cur
            while elem._next!=self._cur:
                if elem._data == x:
                    print ("Елемент знайдено")
                    self._cur = elem
                    b = True
                    break
                elem = elem._next
            if not b: print("Елемент не знайдено")
        return b
    
    def __del__(self):
        '''Закінчити роботу зі списком.
        '''
        if not self.isempty():                       
            while self._cur != None:
                self.delete()
                self.next

S = Rlist()
n = int(input("Кількість елементів списку"))
for i in range(n):
    S.insert(input())
S.print()
print("Поточний елемент", S.getcurrent())
S.next()
S.print()
print("Поточний елемент", S.getcurrent())
print("Кількість елементів", S.len())

S.print()
S.search(input("Введіть елемент для пошуку: "))
S.print()
