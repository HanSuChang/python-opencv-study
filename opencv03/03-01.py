# OpenCV 03 기초 연습 및 실습



# 필터링과 기하학적 변환

# 필터링 (Filtering)과 컨볼루션

#필터링은 커널(Kernel) 또는 마스크(Mask)라고 불리는 작은 행렬을 영상 위로 이동시키며 연산하는 과정입니다. 이를 통해 영상을 흐리게 하거나 선명하게 만들 수 있습니다.

# 블러링 (Blurring) - 부드럽게 만들기

#노이즈를 제거하거나 디테일을 줄일 때 사용합니다.

#**평균 블러 (Average Blur): 이웃 픽셀들의 평균값을 사용. `cv2.blur()`
#가우시안 블러 (Gaussian Blur): 중심에 가까운 픽셀에 가중치를 둠. 자연스러운 흐림 효과. `cv2.GaussianBlur()`
#미디언 블러 (Median Blur): 이웃 픽셀들의 중간값을 사용. 점 잡음(Salt-and-pepper noise) 제거에 탁월. `cv2.medianBlur()`


import cv2
import numpy as np

src = cv2.imread('images/lena.jpg')

# 평균 블러 (5x5 커널)
dst_avg = cv2.blur(src, (5, 5))

# 가우시안 블러 (5x5 커널, 표준편차 0=자동)
dst_gaussian = cv2.GaussianBlur(src, (5, 5), 0)

# 미디언 블러 (커널 크기 5)
dst_median = cv2.medianBlur(src, 5)

cv2.imshow('Original', src)
cv2.imshow('Gaussian', dst_gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()