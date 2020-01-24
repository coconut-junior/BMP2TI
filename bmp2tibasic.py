from PIL import Image

im = Image.open('vanilla.bmp','r')
pix_val = list(im.getdata())

x = 0
y = 0

for p in pix_val:
	if p == 0:
		print('(' + str(y) + ', ' + str(x) + ')')
	x+=1
	if x == 95:
		x = 0
		y+=1