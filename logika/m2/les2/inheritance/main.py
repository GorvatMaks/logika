class Widget():
    #властивості класа (в конструкторі)
    def __init__ (self,text,x,y):
        self.text = text
        self.x = x
        self.y = y
    #методи
    def print_info(self):
        print("Напис:", self.text)
        print("Розташування:", self.x, self.y)

class Button(Widget):
    #доповнені властивості класа (в конструкторі)
    def __init__(self,text,x,y,is_clicked):
        super().__init__(text,x,y)
        self.is_clicked = is_clicked
    
    #нові методи
    def click(self):
        self.is_clicked = True
        print("Асаламалеку брат я тебе записав")

#створи екземпляр класа Button
r = Button("брати участь", 100, 100, False)
r.print_info()

#якщо на питання «Хочете зареєструватися?» користувач відповів «так», то застосуйте метод clicy
y=input("Записати тебе?")
y=y.lower()

if y =='так':
    r.click()
else:
    print("sa")    