from PIL import Image

def merge_images(file1, file2, file3, file4):
    """Merge two images into one, displayed side by side
    :param file1: path to first image file
    :param file2: path to second image file
    :return: the merged Image object
    """
    image1 = Image.open(file1)
    image2 = Image.open(file2)
    image3 = Image.open(file3)
    image4 = Image.open(file4)

    (width1, height1) = image1.size
    (width2, height2) = image2.size

    result_width = width1 + width2
    result_height = height1 + height2

    result = Image.new('RGB', (result_width, result_height))
    result.paste(im=image1, box=(0, 0))
    result.paste(im=image2, box=(width1, 0))
    result.paste(im=image3, box=(0, height1))
    result.paste(im=image4, box=(width1, height1))
    result.save("C:\\Users\\riemang\\Documents\\Personal\\LightChanges\\BlackMarble_diff_A1_color.jpg")

merge_images("C:\\Users\\riemang\\Documents\\Personal\\LightChanges\\diff\\BlackMarble_diff_A1_1_color.jpg",
             "C:\\Users\\riemang\\Documents\\Personal\\LightChanges\\diff\\BlackMarble_diff_A1_2_color.jpg",
             "C:\\Users\\riemang\\Documents\\Personal\\LightChanges\\diff\\BlackMarble_diff_A1_3_color.jpg",
             "C:\\Users\\riemang\\Documents\\Personal\\LightChanges\\diff\\BlackMarble_diff_A1_4_color.jpg")


def background(file1, file2):
    image1 = Image.open(file1)
    image2 = Image.open(file2)
    
    merged = Image.blend(image1, image2, .75)
    #merged = Image.alpha_compisite(image1, image2)
    merged.save("C:\\Users\\riemang\\Documents\\Personal\\LightChanges\\A1_Merged2.jpg")
    
background("C:\\Users\\riemang\\Documents\\Personal\\LightChanges\\BlackMarble_2016_A1.jpg",
           "C:\\Users\\riemang\\Documents\\Personal\\LightChanges\\BlackMarble_diff_A1_color.jpg")
