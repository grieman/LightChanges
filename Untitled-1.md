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

```python

```

### Combine Images

```python
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
```

### Paste over Image

```python
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



overlay_images(square = "A1")
overlay_images(square = "A2")
overlay_images(square = "B1")
overlay_images(square = "B2")
overlay_images(square = "C1")
overlay_images(square = "C2")
overlay_images(square = "D1")
overlay_images(square = "D2")
```