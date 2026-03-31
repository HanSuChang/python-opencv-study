import cv2
import numpy as np

src = cv2.imread('images/lena.jpg')


# 샤프닝 커널 정의 (중심 픽셀 강조).
sharpening_mask = np.array([[-1, -1, -1],
                            [-1,  9, -1],
                            [-1, -1, -1]])

dst_sharp = cv2.filter2D(src, -1, sharpening_mask) # -1은 입력 영상과 같은 깊이 유지


cv2.imshow("dst_sharp", dst_sharp)
cv2.waitKey()
cv2.destroyAllWindows()