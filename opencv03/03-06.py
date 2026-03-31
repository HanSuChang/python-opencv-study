import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('images/lena.jpg')
rows, cols, channels = img.shape


# 원래 위치
pts1 = np.float32([[200,100], [400,100], [200,200]])

# 이동할 위치
pts2 = np.float32([[200,300], [400,200], [200,400]])

cv2.circle(img, (200,100), 10, (255,0,0),-1)
cv2.circle(img, (200,100), 10, (0,255,0),-1)
cv2.circle(img, (200,100), 10, (0,0,255),-1)


# 위치 이동에 따른 변환행렬 구하기
M = cv2.getAffineTransform(pts1, pts2)


dst = cv2.warpAffine(img, M, (cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('image')
plt.subplot(122),plt.imshow(img),plt.title('Affine')
plt.show()




cv2.waitKey(0)
cv2.destroyAllWindows()