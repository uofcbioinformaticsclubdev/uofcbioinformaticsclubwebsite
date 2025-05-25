#this file may contain reused functions
from PIL import Image, ImageOps

#this function corrects image orientation by applying EXIF data to assets
#call applyEXIF any time a picture is orientated the wrong
#Arguments - path: the path name of the image
#Returns - img: returns the img object, usuable by st.image()

def applyEXIF(path):
    img = Image.open(path)
    img = ImageOps.exif_transpose(img)
    return img