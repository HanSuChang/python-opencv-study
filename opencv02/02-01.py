#OpenCV 01 기초 연습 및 실습

#덧셈 연산과 밝기 조절...

#- `cv2.add(src1, src2)`: 포화 연산 (Saturation) 적용.
#  - 255를 넘으면 255로 고정. (흰색이 됨) -> 영상 처리에 적합
#- `numpy +` 연산: 모듈로 연산 (Modulo) 적용.
#   - 255를 넘으면 0부터 다시 시작. (검은색으로 반전될 수 있음)

import cv2
import numpy as np

src = cv2.imread("images/lena.jpg")
val = 200 # 더할 밝기 값

# OpenCV 함수 이용 (추천) -> 밝아짐
dst1 = cv2.add(src, (val, val, val, 0)) # B, G, R    0은 투명도 포함

# numpy 연산 이용 -> 255 넘으면 깨짐
dst2 = src + val

cv2.imshow('OpenCV Add', dst1)
cv2.imshow('Numpy Add', dst2)
cv2.waitKey()