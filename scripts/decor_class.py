def cls_time(cls):
    '''Декоратор @benchmark для обчислення часу виконання функції f.

    '''
    import functools
    def benchmark(f):
        import time
        @functools.wraps(f)             
        def _benchmark(*args, **kw):
            t = time.clock()            #вимірюємо час перед викликом функції
            rez = f(*args, **kw)        #викликаємо f
            t = time.clock() - t        #вимірюємо різницю у часі після виклику функції
            print('{0} time elapsed {1:.8f}'.format(f.__name__, t))
            return rez
        return _benchmark


    orig_init=cls.__init__
    orig_isempty=cls.isempty
    orig_maketree=cls.maketree
    orig_root=cls.root
    orig_leftson=cls.leftson
    orig_rightson=cls.rightson
    orig_updateroot=cls.updateroot
    orig_updateleft=cls.updateleft
    orig_updateright=cls.updateright

    
    @benchmark
    def _init_(self):
        return orig._init(self)

    @benchmark
    def isempty(self):
        return orig_isempty(self)

    @benchmark
    def maketree(self, data, t1, t2):
        return orig_maketree(self, data, t1, t2)

    @benchmark
    def root(self):
        return orig_root(self)

    @benchmark    
    def leftson(self):
        return orig_leftson(self)

    @benchmark
    def rightson(self):
        return orig_rightson(self)

    @benchmark
    def updateroot(self,data):
        return orig_updateroot(self,data)

    @benchmark
    def updateleft(self,t):
        return orig_updateleft(self,t)

    @benchmark
    def updateright(self,t):
        return orig_updateright(self,t)
    

    cls._init=_init_
    cls.isempty=isempty
    cls.maketree=maketree
    cls.root=root
    cls.leftson=leftson
    cls.rightson=rightson
    cls.updateroot=updateroot
    cls.updateleft=updateleft
    cls.updateright=updateright
 
    return cls




@cls_time
class Btree:
    '''Реалізує бінарне дерево.
    '''
    def __init__(self):
        '''Створити порожнє дерево.
        '''
        self._data = None       #навантаження кореня дерева
        self._ls = None         #лівий син
        self._rs = None         #правий син

    def isempty(self):
        '''Чи порожнє дерево?.
        '''
        return self._data == None and self._ls == None and self._rs == None

    def maketree(self, data, t1, t2):
        '''Створити дерево.

        Дані у корені - data, лівий син - t1, правий син - t2
        '''
        self._data = data
        self._ls = t1
        self._rs = t2

    def root(self):
        '''Корінь дерева.
        '''
        if self.isempty():
            print('root: Дерево порожнє')
            exit(1)
        return self._data

    def leftson(self):
        '''Лівий син.
        '''
        if self.isempty():
            t = self
        else:
            t = self._ls
        return t

    def rightson(self):
        '''Правий син.
        '''
        if self.isempty():
            t = self
        else:
            t = self._rs
        return t

    def updateroot(self, data):
        '''Змінити корінь значенням data.
        '''
        if self.isempty(): #якщо дерево порожнє, додати лівого та правого сина
            self._ls = Btree()
            self._rs = Btree()
        self._data = data

    def updateleft(self, t):
        '''Змінити лівого сина значенням t.
        '''
        self._ls = t

    def updateright(self, t):
        '''Змінити правого сина значенням t.
        '''
        self._rs = t

import random


sconst = "зв'язування між об'єктами та методами поняття віртуальних методів поліморфізм"

def makewords(s = sconst):
    '''Будує список слів.

    '''
    words = s.split()
    random.shuffle(words) #перемішує слова у списку
    return words

def _searchplace(w, t1, t2):
    '''Шукає місце для w у дереві t1, використовуючи допоміжне дерево t2.

    Якщо w знайдено у дереві t1, то found == True.
    Якщо w не знайдено, то t1 - порожнє дерево, а t2 - батько t1.
    '''
    found = False
    if not t1.isempty():
        if t1.root() == w: #якщо корінь дорівнює w, то знайшли
            found = True
        elif t1.root() > w:#якщо корінь більше w, то йдемо ліворуч
            t1, t2 = t1.leftson(), t1
            found, t1, t2 = _searchplace(w, t1, t2)
        else:              #якщо корінь менше w, то йдемо праворуч
            t1, t2 = t1.rightson(), t1
            found, t1, t2 = _searchplace(w, t1, t2)
    return found, t1, t2
            
def buildtree(seq):
    '''Будує дерево пошуку t за послідовністю seq.

    '''
    t = Btree()
    if len(seq) > 0:
        t.updateroot(seq[0])    #щоб не розбиратись окремо з першим вузлом дерева
    for w in seq:
        found, t1, t2 = _searchplace(w, t, Btree())
        if not found:
            son = Btree()
            son.updateroot(w)   #утворюємо дерево з 1 вузлом
            if t2.root() > w:
                t2.updateleft(son) #приєднуємо як лівого сина
            else:
                t2.updateright(son)#приєднуємо як правого сина 
    return t
                
def searchtree(w, t):
    '''Шукає w у дереві t.

    '''
    found, t1, t2 = _searchplace(w, t, Btree())
    return found

#if name == '__main__':        
words = makewords()
t = buildtree(words)
print(words)
print('\nВведіть слова. "" - завершення')
while True:
    w = input('?')          #вводимо слова для пошуку у дереві
    if len(w) == 0: break
    found = searchtree(w, t)
    print(found)
