from PIL import Image

data = open("./3pixels.csv","r").read().split("\n")
del(data[0])

img = Image.new(mode = "RGB", size = (301, 41))

for i in data:
    x,y,r,g,b = i.split(",")
    img.putpixel((int(x),int(y)),(int(r),int(g),int(b)))

img.show()