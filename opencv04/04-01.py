## 에지 검출의 기초: 미분과 그라디언트**

##에지(Edge)는 픽셀 값이 급격하게 변하는 지점입니다. 이를 수학적으로 찾기 위해 미분을 사용합니다(당연히 미분을 직접 할 필요는 없음). 영상 처리에서는 인접한 픽셀 간의 차이(Gradient)를 계산합니다.

## 소벨 필터 (Sobel Filter)

##가장 대표적인 1차 미분 연산자입니다. x축(수평)과 y축(수직) 방향의 변화량을 각각 계산합니다.

#- `cv2.Sobel(src, ddepth, dx, dy, ksize)`**
#- `dx=1, dy=0`: 수직선 검출 (가로 방향 변화 감지)
#- `dx=0, dy=1`: 수평선 검출 (세로 방향 변화 감지)


import cv2
import numpy as np

img = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

# dx=1, dy=0: 수직 에지 검출
sobel_x = cv2.Sobel(img, -1, 1, 0, ksize=3) 

# dx=0, dy=1: 수평 에지 검출
sobel_y = cv2.Sobel(img, -1, 0, 1, ksize=3)

cv2.imshow('Sobel X', sobel_x)
cv2.imshow('Sobel Y', sobel_y)
cv2.waitKey(0)
cv2.destroyAllWindows()
