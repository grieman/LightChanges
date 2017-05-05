from PIL import Image
import numpy as np
import math

def bg_changes(square):
    im12 = Image.open(square.join(("2012\\BlackMarble_2012_","_gray.jpg")))
    im16 = Image.open(square.join(("2016\\BlackMarble_2016_","_gray.jpg")))
    dat12 = np.array(im12).astype('int32')
    dat16 = np.array(im16).astype('int32')
    new = dat16 - dat12
    off = dat12 - dat16
    new[new < 0] = 0
    off[off < 0] = 0
    
    out = np.concatenate((np.zeros((21600,21600))[..., np.newaxis], new[...,np.newaxis], off[...,np.newaxis]), axis=2)
    out = out.astype('uint8')
    out = Image.fromarray(out)
    out.save(square.join(("diff\\",".jpg")))

bg_changes(square = "A1")
bg_changes(square = "A2")
bg_changes(square = "B1")
bg_changes(square = "B2")
bg_changes(square = "C1")
bg_changes(square = "C2")
bg_changes(square = "D1")
bg_changes(square = "D2")


#def overlay_images(square):
#	bg = Image.open(square.join(("backgrounds\\BlackMarble_2016_",".jpg"))).convert("RGBA")
#	fg = Image.open(square.join(("diff\\",".jpg")))
#	
#	im16 = Image.open(square.join(("2016\\BlackMarble_2016_","_gray.jpg")))
#	
#	fgdat = np.array(fg).astype('int32')
#	r,g,b = np.split(fgdat,3,2)
#	maskdat = g+b
#	maskdat = np.floor((maskdat[:,:,0] / 255)+.9) * 255
#	maskdat = maskdat.astype('uint8')
#	
#	imgdata = np.array(fg.convert("RGBA"))
#	imgdata[:,:,3] = maskdat
#	foreground = Image.fromarray(imgdata)
#	#out = Image.alpha_composite(bg, foreground)
#	bg.paste(foreground, (0,0), foreground)
#	out.save(square.join(("out\\",".jpg")))


def overlay_images(square):
	bg = Image.open(square.join(("backgrounds\\BlackMarble_2016_",".jpg"))).convert("RGBA")
	fg = Image.open(square.join(("diff\\",".jpg")))
	
	mask = fg.convert('L')
	maskdat = np.array(mask)
	maskdat = np.floor((maskdat / 255)+.99) * 255
	maskdat = maskdat.astype('uint8')
	
	imgdata = np.array(fg.convert("RGBA"))
	imgdata[:,:,3] = maskdat
	foreground = Image.fromarray(imgdata)
	out = Image.alpha_composite(bg, foreground)
	out.save(square.join(("out\\",".jpg")))

overlay_images(square = "A1")
overlay_images(square = "A2")
overlay_images(square = "B1")
overlay_images(square = "B2")
overlay_images(square = "C1")
overlay_images(square = "C2")
overlay_images(square = "D1")
overlay_images(square = "D2")


imageA1 = Image.open("diff\\A1.jpg")
imageA2 = Image.open("diff\\A2.jpg")
imageB1 = Image.open("diff\\B1.jpg")
imageB2 = Image.open("diff\\B2.jpg")
imageC1 = Image.open("diff\\C1.jpg")
imageC2 = Image.open("diff\\C2.jpg")
imageD1 = Image.open("diff\\D1.jpg")
imageD2 = Image.open("diff\\D2.jpg")

(width, height) = imageA1.size

result_width = width * 4
result_height = height * 2

result = Image.new('RGB', (result_width, result_height))
result.paste(im=imageA1, box=(0, 0))
result.paste(im=imageA2, box=(0, height))
result.paste(im=imageB1, box=(width, 0))
result.paste(im=imageB2, box=(width, height))
result.paste(im=imageC1, box=(width*2, 0))
result.paste(im=imageC2, box=(width*2, height))
result.paste(im=imageD1, box=(width*3, 0))
result.paste(im=imageD2, box=(width*3, height))

result.save(square.join(("diff\\merged.jpg")))








bg = Image.open(square.join(("backgrounds\\BlackMarble_2016_",".jpg"))).convert("RGBA")
fg = Image.open(square.join(("diff\\",".jpg")))
out = bg

#fgdat = np.array(fg).astype('int32')
#r,g,b = np.split(fgdat,3,2)
#maskdat = g[:,:,0] + b[:,:,0]
#maskdat = np.floor((maskdat / 255)+.995) * 255
	
fgdat = np.array(fg.convert("1"))
	
#im16 = Image.open(square.join(("2016\\BlackMarble_2016_","_gray.jpg")))
#dat16 = np.array(im16).astype('int32')
#dat16 = np.floor((dat16 / 255)+.9) * 255

imgdata = np.array(fg.convert("RGBA"))
imgdata[:,:,3] = fgdat.astype('uint8')
foreground = Image.fromarray(imgdata)
#out = Image.alpha_composite(bg, foreground)
out.paste(foreground, (0,0), foreground)
out.save(square.join(("out\\",".jpg")))




#im12 = Image.open("2012.jpg").convert('L')
#dat12 = np.array(im12).astype('int32')
#im16 = Image.open("2016.jpg").convert('L')
#dat16 = np.array(im16).astype('int32')
#new = dat16 - dat12
#off = dat12 - dat16
#new[new < 0] = 0
#off[off < 0] = 0
#del dat12; del dat16; del im12; del im16

#out = np.concatenate((np.zeros((21600,21600))[..., np.newaxis], new[...,np.newaxis], off[...,np.newaxis]), axis=2)
#out = out.astype('uint8')
#out = Image.fromarray(out)
#out.save("test.jpg")


def merge_images(square):

    image1 = Image.open(square.join(("diff\\BlackMarble_diff_","_1_color.jpg")))
    image2 = Image.open(square.join(("diff\\BlackMarble_diff_","_3_color.jpg")))
    image3 = Image.open(square.join(("diff\\BlackMarble_diff_","_2_color.jpg")))
    image4 = Image.open(square.join(("diff\\BlackMarble_diff_","_4_color.jpg")))

    (width1, height1) = image1.size
    (width2, height2) = image2.size

    result_width = width1 + width2
    result_height = height1 + height2

    result = Image.new('RGB', (result_width, result_height))
    result.paste(im=image1, box=(0, 0))
    result.paste(im=image2, box=(width1, 0))
    result.paste(im=image3, box=(0, height1))
    result.paste(im=image4, box=(width1, height1))
    result.save(square.join(("diff\\BlackMarble_diff_","_color.jpg")))
    
    
merge_images(square = "A1")
merge_images(square = "A2")
merge_images(square = "B1")
merge_images(square = "B2")
merge_images(square = "C1")
merge_images(square = "C2")
merge_images(square = "D1")
merge_images(square = "D2")



#def background(file1, file2):
#    image1 = Image.open(file1)
#    image2 = Image.open(file2)
#    
#    data = np.array(image2.convert("RGBA"))
#    r,g,b,a = data.T
#    data2 = np.array(image2.convert("1")) * 255
#    data = [r,g,b,a]
#    
#    #merged = Image.blend(image1, image2, .75)
#    #merged = Image.alpha_compisite(image1, image2)
#    #merged.save("A1_Merged2.jpg")
#    
#    image2 = Image.fromarray(data)
#    image1.paste(image2, (0,0), image2)
#    
#    
#    imout.save("A1_imout.jpg")
    
    
    
    
#background("BlackMarble_2016_A1.jpg",
#           "diff\\BlackMarble_diff_A1_color.jpg")

def overlay_images(square):
	bg = Image.open(square.join(("backgounds\\BlackMarble_2016_",".jpg")).convert("RGBA")
	fg = Image.open(square.join(("diff\\BlackMarble_diff_","_color.jpg"))
	
	mask = fg.convert('L')
	maskdat = np.array(mask)
	maskdat = np.floor((maskdat / 255)+.99) * 255
	maskdat = maskdat.astype('uint8')
	
	imgdata = np.array(fg.convert("RGBA"))
	imgdata[:,:,3] = maskdat
	foreground = Image.fromarray(data)
	out = Image.alpha_composite(bg, foreground)
	out.save(square.join(("out\\",".jpg"))
	

cd "C:\Users\riemang\Documents\R\NASA Lights"
from PIL import Image
import numpy as np
image2 = Image.open("diff\\BlackMarble_diff_A1_color.jpg")

image2 = image2.convert('L')
data2 = np.array(image2)
data2 = np.floor((data2 / 255)+.99) * 255
data2 = data2.astype('uint8')


bg = Image.open("BlackMarble_2016_A1.jpg").convert("RGBA")
fg = Image.open("diff\\BlackMarble_diff_A1_color.jpg")

data = np.array(fg.convert("RGBA"))
r,g,b,a = data.T

data[:,:,3] = data2
foreground = Image.fromarray(data)

out = Image.alpha_composite(bg, foreground)
out.save("test.jpg")