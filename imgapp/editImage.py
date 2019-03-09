import cv2
from django.conf import settings

def editImage(url, description):

    path = settings.BASE_DIR + url
    img = cv2.imread(path)
    edittedImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    output = settings.BASE_DIR + "/media/edittedImg/" + description + "_gray.jpg"
    cv2.imwrite(output, edittedImg)
