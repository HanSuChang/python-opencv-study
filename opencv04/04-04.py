# 허프 원 검출.

### 원 검출 (Hough Circle Transform)

#`cv2.HoughCircles(image, method, dp, minDist, param1, param2, minRadius, maxRadius)`**
# - 에지 이미지가 아닌 **그레이스케일 이미지**를 입력으로 받습니다. (내부적으로 Canny 적용)
#  - `minDist`: 검출된 원 중심 간의 최소 거리 (너무 가까우면 중복 제거)


import cv2
import numpy as np

src = cv2.imread('images/shape.png')
if src is None:
    print("이미지를 불러올 수 없음")
    exit()

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)


circles1 = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=100, param2=20, minRadius=10, maxRadius=100)

if circles1 is not None:

    circles1 = np.uint16(np.around(circles1))

    for circle in circles1[0, :]:
        cx, cy, r = circle

        cv2.circle(src, (int(cx), int(cy)), int(r), (0, 0, 255), 2)

cv2.imshow('src', src)
cv2.waitKey()
cv2.destroyAllWindows()