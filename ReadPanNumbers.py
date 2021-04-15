
import os, io
from google.cloud import vision 

def getInfo(img_name):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'D:\Ansh\Python\Internship\Token.json'

    client = vision.ImageAnnotatorClient()

    folder_add = r'D:\Ansh\Python\Internship'

    with io.open(os.path.join(folder_add,img_name), 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content = content)

    response = client.text_detection(image = image)

    t = response.text_annotations

    for i in t:
        x = str(i.description)
        if isValid(x):
            return x
    return None


def isValid(pan_number):
    if len(pan_number) != 10:
        return False
    for i in range(5):
        if pan_number[i] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return False
    for i in range(5,9):
        if pan_number[i] not in '0123456789':
            return False
    if pan_number[-1] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        return False
    return True
  
pan_number = getInfo('Example_pan.png')
