from PIL import Image
import numpy as np
import math

im12 = Image.open("2012.jpg")
dat12 = np.array(im12)
im16 = Image.open("2016.jpg")
dat16 = np.array(im16)
new = dat16 - dat12
off = dat12 - dat16
new[new < 0] = 0
off[off < 0] = 0

out = np.concatenate((np.zeros((21600,21600))[..., np.newaxis], new[...,np.newaxis], off[...,np.newaxis]), axis=2)

def merge_images(square):
    """Merge two images into one, displayed side by side
    :param file1: path to first image file
    :param file2: path to second image file
    :return: the merged Image object
    """
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