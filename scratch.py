from PIL import Image
from PIL import ImageChops
import numpy as np
 
image_2016 = Image.open("C:\\Users\\riemang\\Documents\\Personal\\LightChanges\\BlackMarble_2016_A1_gray.jpg")
image_2012 = Image.open("C:\\Users\\riemang\\Documents\\Personal\\LightChanges\\BlackMarble_2012_A1_gray.jpg")

turned_on  = np.array(image_2016) - np.array(image_2012)
turned_off = np.array(image_2012) - np.array(image_2016)
del image_2012
del image_2016

turned_on = Image.fromarray(turned_on).convert("RGB")
turned_on = np.array(turned_on)
turned_on[:,:,0] *=0
turned_on[:,:,1] = np.array(Image.fromarray(turned_off).convert("RGB"))[:,:,1] #green = turned off
turned_on = Image.fromarray(turned_on) #converted to blue
 
#turned_off = Image.fromarray(turned_off).convert("RGB")
#turned_off = np.array(turned_off)
#turned_off[:,:,0] *=0
#turned_off[:,:,2] *=0
#turned_off = Image.fromarray(turned_off) #converted to green
 


#diff = ImageChops.difference(image_2012, image_2016)

if turned_on.getbbox():
        turned_on.save("C:\\Users\\riemang\\Documents\\Personal\\LightChanges\\BlackMarble_A1.jpg")




