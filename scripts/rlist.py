#T14s2_11
#Кільцевий список

class Rlist:
    '''Реалізує кільцевий список на базі списку.
    '''
    def __init__(self):
        '''Створити порожній список.
        '''
        self._lst = []                  #список елементів
        self._cur = None                #індекс поточного елемента

    def len(self):
        '''Довжина списку.
        '''
        return len(self._lst)

    def next(self):
        '''Перейти до наступного елемента.
        '''
        l = self.len()
        if l != 0:
            if self._cur == l-1:    #для (l-1) елемента наступним буде нульовий
                self._cur = 0
            else:
                self._cur += 1

    def getcurrent(self):
        '''Повернути поточний елемент.
        '''
        if self.len() == 0:
            print('getcurrent: список порожній')
            exit(1)
        data = self._lst[self._cur]
        return data

    def update(self, data):
        '''Оновити поточний елемент.
        '''
        if self.len() == 0:
            print('update: список порожній')
            exit(1)
        self._lst[self._cur] = data

    def insert(self, data):
        '''Вставити елемент перед поточним.
        '''
        if self.len() == 0:             #якщо список порожній
            self._lst.append(data)      #додаємо елемент, він стає поточним
            self._cur = 0
        else:
            self._lst.insert(self._cur,data) #інакше вставляємо елемент перед поточним
            self._cur += 1                   #щоб поточний елемент не змінився, треба індекс збільшити на 1   

    def delete(self):
        '''Видалити поточний елемент.
        '''
        if self.len() == 0:
            print('delete: список порожній')
            exit(1)
        l = self.len()
        del self._lst[self._cur]
        if l == 1:                  #якщо список після видалення елемента спорожніє
            self._cur = None
        elif self._cur == l-1:      #якщо поточним був останній елемент списку
            self._cur = 0           #поточним стане елемент з індексом 0
        #else: pass                  якщо поточним був не останній елемент, нічого не робити
                                                            
    def __del__(self):
        '''Закінчити роботу зі списком.
        '''
        del self._lst
