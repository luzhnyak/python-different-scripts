#T14s3_01
#Бінарне дерево


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


#sconst = "зв'язування між об'єктами та методами поняття віртуальних методів поліморфізм"
sconst = "6 4 8 2 3 5 7 1 9 0 q f t x i e x t"

def makewords(s = sconst):
    '''Будує список слів.

    '''
    words = s.split()
    #random.shuffle(words) #перемішує слова у списку
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


# /* Висота дерева */

def height(t):
      if t==None:
          return 0
      else:
        lheight = height(t._ls)
        rheight = height(t._rs)
    
        if lheight > rheight:
            return(lheight+1)
        else:
          return(rheight+1)
        

# /* Формуэмо список з елементів рівня */
def levelDerevo(t, level):    
    if t == None:
        return    
    global riven    
    if level == 1:
        if t._data!=None:
            riven.append(t._data)
        else:
            riven.append(" ")
    elif level > 1:
        levelDerevo(t.leftson(), level-1);
        levelDerevo(t.rightson(), level-1);
    


# /* функція для друку дерева */
def printDerevo(t):
      h = height(t)
      i=1
      global riven
      rtemp=[]
      rtemp.append(1)
      kp=int(2**(h-1)-1)      
      while(i<=h-1):        
        riven=[]
        levelDerevo(t, i)
        # Відстань між елементами рівня
        vidstup=""
        pid=""
        j=0
        for j in range(kp):
            vidstup=vidstup+" "
            pid=pid+"─"
        iii=int(len(pid)/2)
        pid=pid[:iii]+"┴"+pid[iii+1:]
        kp=int((kp-1)/2)
        # Відступ від початку
        pr=""
        j=0
        for j in range(kp):
            pr=pr+" "        
        # Добавляємо елементи рівня
        k=0
        pidkr=pr
        p=True
        for e in range(len(riven)):
            if e!=len(riven)-1:            
                pr=pr+riven[e]+vidstup
            else:
                pr=pr+riven[e]
            if p:
                if riven[e]!=" " or riven[e+1]!=" ":
                    pidkr=pidkr+"┌"+pid+"┐"
                    p=False
                else:
                    pidkr=pidkr+" "+vidstup+" "
                    p=False
            else:
                if e!=len(riven)-1:
                    pidkr=pidkr+vidstup
                    p=True

#str(len(riven))
        if i>1: print(pidkr)
        print(pr)
        rtemp=riven
        i +=1


if __name__ == '__main__':        
    words = makewords()
    t = buildtree(words)
    print(words)    
    print('\nВведіть слова. "" - завершення')
    while True:
        w = input('?')          #вводимо слова для пошуку у дереві
        if len(w) == 0: break
        found = searchtree(w, t)
        print(found)
        

print("Висота дерева:", height(t))
printDerevo(t)
