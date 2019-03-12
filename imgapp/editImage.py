import cv2
from django.conf import settings

def setLabelCvtType(cvt_param):
    if cvt_param == "gray":
        cvt_type = "白黒画像"
    else:
        cvt_type = ""
    return cvt_type

def editImage(url, name, cvt_param):
    if cvt_param == "gray":
        convertToGray(url, name, cvt_param)

def convertToGray(url, name, cvt_param):
    path = settings.BASE_DIR + url
    img = cv2.imread(path)
    edittedImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    output = settings.BASE_DIR + "/media/edittedImg/" + name + "_gray.jpg"
    cv2.imwrite(output, edittedImg)

def setOutputPath(name, cvt_param):
    output = "edittedImg/" + name + "_" + cvt_param +".jpg"
    return output
