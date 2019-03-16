import cv2
from django.conf import settings
from .mosaic import mosaic as mosaic
import numpy as np

def setLabelCvtType(cvt_param):
    if cvt_param == "gray":
        cvt_type = "グレースケール画像"
    elif cvt_param == "monochrome":
        cvt_type = "モノクロ画像"
    elif cvt_param == "mosaic":
        cvt_type = "顔モザイク画像"
    elif cvt_param == "convolute":
        cvt_type = "ぼかし画像"

    return cvt_type

def editImage(url, name, cvt_param):
    if cvt_param == "gray":
        convertToGray(url, name, cvt_param)
    elif cvt_param == "monochrome":
        convertToThreshold(url, name, cvt_param)
    elif cvt_param == "mosaic":
        convertToMosaic(url, name, cvt_param)
    elif cvt_param == "convolute":
        convolute(url, name, cvt_param)

# グレースケールに変換
def convertToGray(url, name, cvt_param):
    img = readImg(url)
    edittedImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    output = decideOutputPath(name, cvt_param)
    cv2.imwrite(output, edittedImg)

# モノクロ画像に変換
# グレースケールに変換+閾値処理
def convertToThreshold(url, name, cvt_param):
    img = readImg(url)
    # 閾値を指定
    threshhold = 150
    # グレースケール化
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 画像の2値化
    retval, edittedImg = cv2.threshold(grayImg, threshhold, 255, cv2.THRESH_BINARY)
    output = decideOutputPath(name, cvt_param)
    cv2.imwrite(output, edittedImg)

# モザイク画像に変換
def convertToMosaic(url, name, cvt_param):
    # カスケードファイルを指定して、検出器を作成
    cascade_file = settings.BASE_DIR + "/imgapp/cascade/haarcascade_frontalface_alt.xml"
    # カスケード分類器のファイルを読み込む
    cascade = cv2.CascadeClassifier(cascade_file)

    # 画像を読み込んでグレースケールに変換
    img = readImg(url)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 顔認識を実行 顔の位置の配列(x,y,w,h)
    face_list = cascade.detectMultiScale(img_gray,minSize =(50,50))

    # 結果を確認
    if len(face_list) == 0:
        pass

    # 認識した部分にモザイク
    for(x,y,w,h) in face_list:
        # mosaic(画像ファイル,(左上x,左上y,右下x, 右下y), ratio)
        edittedImg = mosaic(img,(x,y,x + w, y + h), 15)
    output = decideOutputPath(name, cvt_param)
    cv2.imwrite(output, edittedImg)

def convolute(url, name, cvt_param):
    img = readImg(url)
    # 5*5のウィンドウを指定して、25で平均値をとる
    kernel = np.ones((10,10),np.float32)/100
    edittedImg = cv2.filter2D(img,-1,kernel)
    output = decideOutputPath(name, cvt_param)
    cv2.imwrite(output, edittedImg)

# 画像を読みこむ
def readImg(url):
    path = settings.BASE_DIR + url
    img = cv2.imread(path)
    return img


# DBに保存する加工画像のパスを算出
def setOutputPath(name, cvt_param):
     output = "edittedImg/" + name + "_" + cvt_param +".jpg"
     return output

# DBに保存する加工画像のパスを算出
def decideOutputPath(name, cvt_param):
    output = settings.BASE_DIR + "/media/edittedImg/" + name + "_" + cvt_param +".jpg"
    return output
