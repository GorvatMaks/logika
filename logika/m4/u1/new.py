from PIL import Image, ImageFilter

class ImageEditor():
    def __init__(self, filename):
        self.filename = filename
        self.original = None
        self.changed = []

    def open(self):
        try:
            self.original = Image.open(self.filename)
            print(self.original.size)
            #self.original.show()
        except:
            print('Файлу не найдено')

    def do_left(self):
        left = self.original.transpose(Image.ROTATE_90)
        self.changed.append(left)

        left.save('Rotete_'+ self.filename)

    def do_cropp(self):
        box = (2,1,5,8)
        cropp = self.original.crop(box)    
        cropp.show()
        cropp.save('cropp_'+ self.filename)

    


img = ImageEditor('photo.jpg')
img.open()
img.do_cropp()

