import datetime
import pickle

class Genre:
    def __init__(self):
        self.name = None
        self.characteristic = None

    def inputG(self):
        self.name = input('Імя жанру ')
        self.characteristic = input('Характерні особливості ')      

    def printG(self):
        print(self.name, self.characteristic, end = ' ')
        
class Carrier:
    def __init__(self):
        self.nosiy = None
        self.colors = None
        self.time = None

    def inputC(self):
        self.nosiy = input('Тип носія ')
        self.colors = input('Кольорова гама ')
        self.time = int(input('Тривалість зберігання'))

    def printC(self):
        print(self.nosiy, self.colors, self.time, end = ' ')

class Film(Genre,Carrier):
    def __init__(self):
        Genre.__init__(self)
        Carrier.__init__(self)
        self.title = None
        self.writer = None
        self.director = None
        self.duration = None
        self.year = None

    def inputF(self):
        self.title = input('Назва фільму ')
        self.writer = input('Автор сценарію ')
        self.director = input('Режисер ')
        self.duration = input('Тривалість ')
        self.year = int(input('Рік запису '))
        Genre.inputG(self)
        Carrier.inputC(self)

    def printF(self):             
        print(self.title, self.writer, self.director, self.duration, self.year, end = ' ')
        Genre.printG(self)
        Carrier.printC(self)
        print(' ') 

filmoteka=[]
diya=''
d=datetime.datetime.now()
y=d.year
try:
    file = open('filmoteka.dat','rb')
    filmoteka = pickle.load(file)   #завантажуємо сховище фільмів з файлу у список filmoteka
    file.close()
except EOFError:
    print("Файл сховища пустий\n")
while diya!='4':
    print('Виберіть дію:');
    diya = input('1 - додати фільм, 2 - вивести фільми, 3 - зберегти на диск, 4 - вихі з програми ')
    if diya=='1':
        f = Film()
        f.inputF()
        filmoteka.append(f)                                         
    elif diya=='2':
        filtr=''
        print('Виберіть фільтр:');
        filtr = input('1 - усі фільми, 2 - носій, 3 - автор, 4 - режесер, 5 - час зберігання')
        if filtr=='1':
            for f in filmoteka:
                f.printF()
        elif filtr=='2':
            nosiy = input('Введіть носій ')
            for f in filmoteka:
                if nosiy==f.nosiy: f.printF()
        elif filtr=='3':
            writer = input('Введіть автора ')
            for f in filmoteka:
                if writer==f.writer: f.printF()
        elif filtr=='4':
            director = input('Введіть режесера ')
            for f in filmoteka:
                if writer==f.writer: f.printF()
        elif filtr=='5':
            time = int(input('Введіть час зберігання '))                        
            for f in filmoteka:                
                if time<=f.time-(y-f.year): f.printF()
    elif diya=='3':
        file = open('filmoteka.dat','wb')
        pickle.dump(filmoteka,file)     #записуємо сховище фільмів  у файл
        file.close()
