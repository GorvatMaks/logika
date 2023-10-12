from PIL import Image, ImageFilter

with Image.open('photo.jpg') as orig:
    print(orig.size)
    print(orig.format)
    print(orig.mode)

    bw_or = orig.convert('L')
    bw_or.show()
    bw_or.save('lets.jpg')
    
    blur_or = orig.filter(ImageFilter.BLUR)
    blur_or.show()
    blur_or.save('lets1.jpg')

    pic_up = orig.transpose(Image.ROTATE_180)
    pic_up.show()
    pic_up.save('lets180.jpg')