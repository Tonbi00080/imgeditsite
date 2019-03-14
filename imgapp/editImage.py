import cv2
from django.conf import settings

def setLabelCvtType(cvt_param):
    if cvt_param == "gray":
        cvt_type = "グレースケール画像"
    elif cvt_param == "monochrome":
        cvt_type = "モノクロ画像"
    return cvt_type

def editImage(url, name, cvt_param):
    if cvt_param == "gray":
        convertToGray(url, name, cvt_param)
    elif cvt_param == "monochrome":
        convertToThreshold(url, name, cvt_param)

def convertToGray(url, name, cvt_param):
    path = settings.BASE_DIR + url
    img = cv2.imread(path)
    edittedImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    output = settings.BASE_DIR + "/media/edittedImg/" + name + "_gray.jpg"
    cv2.imwrite(output, edittedImg)

def convertToThreshold(url, name, cvt_param):
    path = settings.BASE_DIR + url
    img = cv2.imread(path)
    # 閾値を指定
    threshhold = 150
    # グレースケール化
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 画像の2値化
    retval, edittedImg = cv2.threshold(grayImg, threshhold, 255, cv2.THRESH_BINARY)
    output = settings.BASE_DIR + "/media/edittedImg/" + name + "_monochrome.jpg"
    cv2.imwrite(output, edittedImg)

def setOutputPath(name, cvt_param):
    output = "edittedImg/" + name + "_" + cvt_param +".jpg"
    return output
