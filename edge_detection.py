import cv2
from matplotlib import pyplot as plt
img = cv2.imread("image2.jpeg", 0)
edges = cv2.Canny(img, 200, 300)
plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 2, 2), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()