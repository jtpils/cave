import cv2
import numpy as np
import ipdb

ipdb.set_trace(context=5)

img = cv2.imread("image2.jpeg", 0)
img = cv2.Canny(img, 200, 300)

ret, th = cv2.threshold(img, 127, 255, 0)

image, contours, hierarchy = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

color = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2BGR)

img = cv2.drawContours(color, contours, -1, (0, 255, 0), 2)
cv2.imwrite("contours.png", color)
cv2.waitKey()
cv2.destroyAllWindows()