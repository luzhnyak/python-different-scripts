class Multimnogina:
    def __init__(self):
        self.mset= {}

    def pusta(self):
        if len(self.mset)>0:
            print(True)
        else: print(False)

    def add(self,k):
        self.mset[k]=self.mset.get(k,0)+1


    def exclude(self):
        k=input('Введіть елемент')
        if (self.mset.get(k,0))!=0:
            self.mset[k]=self.mset.get(k,0)-1
        if (self.mset.get(k,0))==0:
            del self.mset[k]
    def print(self):
        print(self.mset)

    def count(self,k):
        return self.mset.get(k)

    def sort(self):
        p=list(self.mset)
        p.sort()
        r={}
        for i in p:
            r[i]=self.mset.get(i)
        self.mset=r
        
def obyednanya(p1,p2):
    p=p1.copy()
    for k in p2.keys():
        if p.get(k,0)<=p2.get(k,0):
            p[k]=p2.get(k)    
    return p

        
def peretun(p1,p2):    
    p=p1.copy()
    for k in p2.keys():
        if p.get(k,0)>=p2.get(k,0):
            p[k]=p2.get(k)
        if p.get(k,0)==0:
            p[k]=p2.get(k)    
    return p
        
        
l1=input('Введіть рядок1 ')
l2=input('Введіть рядок2 ')
                
s2=Multimnogina() 
for i in range(len(l2)):
    s2.add(l2[i])

s1=Multimnogina()                
for i in range(len(l1)):
    s1.add(l1[i])
    

s1.print()
s2.print()

if s2.mset == s1.mset:
    print('True')
else:
    print('False')
    

ob=Multimnogina() 
ob.mset=obyednanya(s1.mset,s2.mset)
ob.print()


pr=Multimnogina() 
pr.mset=peretun(s1.mset,s2.mset)
pr.print()
