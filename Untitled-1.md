---
title: 
date: 
tags: 
- 
- 
---

## Earth at Night

Recently I found [this](https://blogs.esri.com/esri/arcgis/2017/04/28/lights-on-lights-out/) blog post which compared NASA's [Earth at Night](https://earthobservatory.nasa.gov/Features/NightLights/page3.php) images from 2012 and 2016. They used ArcGIS to produce this map by manipulating and combining the two NASA images, producing [this visually appealing image](http://openseadragon.github.io/openseadragonizer/?img=https%3A%2F%2Fadventuresinmapping.files.wordpress.com%2F2017%2F04%2Fachangingearthatnight.jpg&encoded=true). However, it is hard to extract much more than general information from it. The author states that blue corresponds to new lights coming on, while pink signifies lights going off - this is likely true in most cases, but since the brightest areas may have gotten even brighter over the four years, they could have made unchanged lighting look dimmer by comparison, causing it to dim in the image. There's also no way to see the magnitute of change at any pixel, just the direction.  
Seeking to emulate this and pick up some new python skills, I tried to do an analysis of my own.

### Calculating Differences

As NASA provided eight subimages, I used those to make the processes less memory intensive while maintaining a high image quality. 

The first step was to find which pixels changed between the two images, and quantify that change. I wanted the end result to be an image - with green values denoting brighter pixels and blue darker. Loading the images with Python Imaging Library (PIL), they were converted to numpy arrays and the difference between them was calculated. Any negative values were set to zeros. Lastly, the two arrays were combined with an array of zeros to make a color image which was then saved.

```python
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
```

![](/images/BlackMarble/diff_C1.jpg)

### Making the Data Recognizable

This image has all the desired information, but with only lights it's not immediately apparent which cities and places are which without a substantial knowledge of geography. To make it easier, I overlaid the image from above onto the other image provided by NASA, with some topographical images.

In my opinion, is a bit less informative than the previous version, since some of the changes were blurred out during image processing or hard to identify against the color of the background. 

```python
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
```
![](/images/BlackMarble/background_C1.jpg)

### Combine Images

```python
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

result.save("diff\\merged.jpg")
```